import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:
    @staticmethod
    def get_driver(browser='chrome'):
        WIDTH = 1920
        HEIGHT = 1080

        is_headless = os.environ.get('HEADLESS', 'false').lower() == 'true'

        if browser.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument('--incognito')
            options.add_argument(f'--window-size={WIDTH},{HEIGHT}')
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

            if is_headless:
                print("Running Chrome in Headless Mode.")
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')

            driver = webdriver.Chrome(options=options)

        elif browser.lower() == 'firefox':
            options = FirefoxOptions()
            if is_headless:
                options.add_argument('--headless')

            options.add_argument(f'-width={WIDTH}')
            options.add_argument(f'-height={HEIGHT}')

            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Browser '{browser}' is not supported")

        return driver
