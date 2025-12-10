from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.application_url import ApplicationUrl


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove-sauce-labs-']")

    def navigate_to_cart_page(self):
        self.driver.get(f"{ApplicationUrl.BASE.value}/{ApplicationUrl.CART.value}")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def get_cart_items_count(self):
        return len(self.driver.find_elements(self.CART_ITEMS))

    def remove_item_by_index(self, index):
        remove_buttons = self.driver.find_elements(self.REMOVE_BUTTONS)
        self.click(remove_buttons[index])

    def get_first_item_name(self):
        items = self.driver.find_elements(self.ITEM_NAME)
        if items:
            return items[0].text
        return None
