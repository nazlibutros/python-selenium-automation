# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep

#
#
#
# # previous version - without variables
# # @when('Search for coffee')
# # def search_product(context):
# #     context.driver.find_element(By.ID, 'search').send_keys('coffee')
# #     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
# #     sleep(6)  # wait for ads to disappear
#
# # with variables- dynamic steps
#
#
# @then('Verify search worked for {expected_product}')
# def verify_search(context, expected_product):
#     search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
#     assert expected_product in search_results_header, f'Expected text coffee not in {search_results_header}'
#
#
# @then('Verify {expected_url} in search result url')
# def verify_search_url(context, expected_url):
#     assert expected_url in context.driver.current_url
#
#
# @when('Click on cart icon')
# def click_product(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#     sleep(6)  # wait for ads to disappear
#
#
# @then('Verify cart is empty message shown')
# def verify_search_cart(context):
#     search_results_header = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
#     print(search_results_header)
#     assert 'Your cart is empty' in search_results_header, f'Expected text Your cart is empty not in {search_results_header}'
#
#
# # "//h1[@class*='StyledHeading'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from behave import given, when, then

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # find_element by default it will pick 1st one
    # all_buttons = context.driver.find_elements(*ADD_TO_CART_BTN)
    # all_buttons[2].click()


@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not shown in side navigation'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@then('Verify search worked for {product}')
def verify_search(context, product):
    # search_results_header = context.driver.find_element(*SEARCH_RESULT_TXT).text
    # assert product in search_results_header, \
    #     f'Expected text {product} not in {search_results_header}'
    context.app.search_results_page.verify_search_result(product)


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    # assert expected_keyword in context.driver.current_url, \
    #     f'Expected keyword: {expected_keyword} not in {context.driver.current_url}'
    context.app.search_results_page.verify_search_url(expected_keyword)


@then('Verify every product has a name and an image')
def verify_products_name_img(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(3)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'product title not shown'
        product.find_element(*PRODUCT_IMG)


# @then('Verify search worked')