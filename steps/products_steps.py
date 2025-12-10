from behave import then, when
from pages.products_page import ProductsPage


@then('all products should have a name and a price greater than 0')
def step_validate_products(context):
    products_page = ProductsPage(context.driver)
    items = products_page.get_all_product_data()

    for item in items:
        assert len(item['name']) > 0, "Product name is empty"
        assert item['price'] > 0, f"Product price is 0 for {item['name']}"


@when('I sort items by "{sort_option}"')
def step_sort_items(context, sort_option):
    products_page = ProductsPage(context.driver)
    products_page.select_sort_option(sort_option)


@then('the products should be sorted by price ascending')
def step_verify_sort_asc(context):
    verify_price_sort(context, reverse=False)


@then('the products should be sorted by price descending')
def step_verify_sort_desc(context):
    verify_price_sort(context, reverse=True)


def verify_price_sort(context, reverse=False):
    products_page = ProductsPage(context.driver)
    prices = products_page.get_all_prices()
    expected_sorted_prices = sorted(prices, reverse=reverse)
    sort_order = "high to low" if reverse else "low to high"
    error_message = f"Prices are not sorted {sort_order}"
    assert prices == expected_sorted_prices, error_message
