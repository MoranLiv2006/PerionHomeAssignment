from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from utils.application_url import ApplicationUrl


class ProductsPage(BasePage):
    PRODUCTS_HEADER = (By.CSS_SELECTOR, "span[data-test='title']")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart-']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove-']")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def wait_for_inventory_page(self):
        return self.find(self.PRODUCTS_HEADER).is_displayed() and (
                ApplicationUrl.INVENTORY.value in self.driver.current_url)

    def get_all_product_data(self):
        products = []
        for element in self.driver.find_elements(*self.PRODUCT_LIST):
            name = element.find_element(*self.ITEM_NAME).text
            price_text = element.find_element(*self.ITEM_PRICE).text
            price = float(price_text.replace('$', ''))

            products.append({'name': name, 'price': price})

        return products

    def get_all_prices(self):
        return [p['price'] for p in self.get_all_product_data()]

    def select_sort_option(self, option_text):
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_visible_text(option_text)

    def add_item_to_cart_by_index(self, index):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if index < len(add_buttons):
            add_buttons[index].click()

    def remove_item_by_index(self, index):
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        if index < len(remove_buttons):
            remove_buttons[index].click()

    def get_cart_badge_text(self):
        try:
            return self.get_text(self.SHOPPING_CART_BADGE)
        except NoSuchElementException:
            return "0"
