from behave import when, then
from pages.products_page import ProductsPage

@when('I add the first "{count}" items to the cart')
def step_add_items(context, count):
    context.products_page = ProductsPage(context.driver)
    for i in range(int(count)):
        context.products_page.add_item_to_cart_by_index(i)

@then('the cart badge should display "{count}"')
def step_check_badge(context, count):
    products_page = ProductsPage(context.driver)
    badge_text = products_page.get_cart_badge_text()
    assert badge_text == count, f"Expected {count} in badge, got {badge_text}"

@when('I remove the first item from the cart')
def step_remove_item(context):
    products_page = ProductsPage(context.driver)
    products_page.remove_item_by_index(0)