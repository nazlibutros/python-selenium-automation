from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


@when('Open cart page')
def open_cart(context):
    # context.driver.get('https://www.target.com/cart')
    context.app.cart_page.open_cart_page()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name(context.product_name)
    # actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    # assert context.product_name == actual_name, f'Expected {context.product_name}, but got {actual_name}'


@then('Verify cart has {amount} item(s)')
def verify_cart_item(context, amount):
    context.app.cart_page.verify_cart_item_amount(amount)
    # summary_text = context.driver.find_element(*CART_SUMMARY).text
    # assert f'{amount} item' in summary_text, f"Expected '{amount} item' not in {summary_text}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_items(context):
    # message = context.driver.find_element(*CART_EMPTY_MESSAGE).text
    # print(message)
    # assert message == 'Your cart is empty', f'Expected Your cart is empty, but got {message}'
    context.app.cart_page.verify_cart_empty_txt()
