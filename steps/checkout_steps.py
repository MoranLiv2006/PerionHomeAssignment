import csv
from behave import given, when, then
from selenium.common import NoSuchElementException

from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import os

from utils.application_url import ApplicationUrl


@given('I have "{count}" items in my cart')
def step_setup_cart(context, count):
    products_page = ProductsPage(context.driver)
    context.driver.get(ApplicationUrl.INVENTORY.value)

    for i in range(int(count)):
        products_page.add_item_to_cart_by_index(i)


@given('my cart is empty')
def step_empty_cart(context):
    context.driver.get(ApplicationUrl.INVENTORY.value)
    try:
        cart_page = CartPage(context.driver)
        cart_page.navigate_to_cart_page()
        while cart_page.get_cart_items_count() > 0:
            cart_page.remove_item_by_index(0)
    except NoSuchElementException:
        pass


@when('I try to navigate to checkout')
def step_try_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.navigate_to_cart_page()
    context.cart_page.click_checkout()


@then('the system should prevent checkout or show an error')
def step_verify_checkout_prevention(context):
    context.checkout_page = CheckoutPage(context.driver)
    try:
        error = context.checkout_page.get_error_message()
        assert "Error" in error or "Your cart is empty" in context.driver.page_source
    except NoSuchElementException:
        assert ApplicationUrl.CART.value in context.driver.current_url or ApplicationUrl.CHECKOUT_STEP_ONE.value not in context.driver.current_url


@given('I proceed to the checkout page')
def step_go_to_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.navigate_to_cart_page()
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.driver)
    assert f"{ApplicationUrl.CHECKOUT_STEP_ONE.value.split('.html')[0]}" in context.driver.current_url


@when('I fill checkout information from "{filename}"')
def step_fill_checkout_csv(context, filename):
    file_path = os.path.join('data', filename)

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = next(reader)

    context.checkout_page.fill_info(data['first_name'], data['last_name'], data['zip'])
    context.checkout_page.click_continue()
    assert f"{ApplicationUrl.CHECKOUT_STEP_TWO.value.split('.html')[0]}" in context.driver.current_url


@then('the Item total plus Tax should equal the Total amount')
def step_validate_math(context):
    item_total, tax, grand_total = context.checkout_page.get_prices_as_float_and_without_symbols()
    calculated_total = round(item_total + tax, 2)
    assert calculated_total == grand_total, \
        f"Order Summary Math Error: {item_total} + {tax} = {calculated_total}, expected {grand_total}"


@when('I finish the order')
def step_finish_order(context):
    context.checkout_page.click_finish()


@then('I should see the order completion message "{message}"')
def step_verify_success(context, message):
    success_text = context.checkout_page.get_complete_header()
    assert message in success_text, f"Expected success message '{message}', got '{success_text}'"
