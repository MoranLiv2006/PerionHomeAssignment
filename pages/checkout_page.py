from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first_name, last_name, zip_code):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.ZIP_CODE_INPUT, zip_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def extract_float_from_texted_number(self, element):
        element_text = self.find(element).text
        return float(element_text.split('$')[-1])

    def get_prices_as_float_and_without_symbols(self):
        return (self.extract_float_from_texted_number(self.ITEM_TOTAL),
                self.extract_float_from_texted_number(self.TAX),
                self.extract_float_from_texted_number(self.TOTAL),)

    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
