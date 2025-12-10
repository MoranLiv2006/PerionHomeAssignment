import os

from utils.driver_factory import DriverFactory


def before_all(context):
    browser_name = os.environ.get('BROWSER', 'chrome')
    context.driver = DriverFactory.get_driver(browser_name)


def after_step(context, step):
    if step.status == "failed":
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        filename = f"screenshots/{step.name.replace(' ', '_')}.png"
        context.driver.save_screenshot(filename)


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
