from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
