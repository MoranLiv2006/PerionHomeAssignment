from enum import Enum


class ApplicationUrl(Enum):
    BASE = "https://www.saucedemo.com/"
    INVENTORY = f"{BASE}inventory.html"
    CART = f"{BASE}cart.html"
    CHECKOUT_STEP_ONE = f"{BASE}checkout-step-one.html"
    CHECKOUT_STEP_TWO = f"{BASE}checkout-step-two.html"
