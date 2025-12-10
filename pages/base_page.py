from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def enter_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, element):
        return self.find(element).text
