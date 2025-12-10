import json

from behave import given, when, then

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.application_url import ApplicationUrl

with open("data/users.json") as f:
    USER_DATA = json.load(f)


@given('I am on the login page')
def step_open_login(context):
    context.driver.get(ApplicationUrl.BASE.value)
    context.login_page = LoginPage(context.driver)


@given('I am logged in as "{user_key}"')
def step_login_background(context, user_key):
    step_open_login(context)
    step_login_action(context, user_key)


@when('I login with user "{user_type}"')
def step_login_action(context, user_type):
    password = USER_DATA[user_type]
    context.login_page.login(user_type, password)
    context.products_page = ProductsPage(context.driver)


@then('I should see the "{expected_result}"')
def step_check_result(context, expected_result):
    if "inventory page" in expected_result:
        assert context.products_page.wait_for_inventory_page(), \
            "Expected Inventory page was not displayed after successful login."

    elif "Epic sadface" in expected_result:
        assert ApplicationUrl.INVENTORY.value not in context.driver.current_url
        error_msg = context.login_page.get_error_message()
        assert expected_result in error_msg

    else:
        raise ValueError(f"Unknown expected result type: {expected_result}")
