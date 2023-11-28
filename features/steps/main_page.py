# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @given('Open target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('Search for {product}')
# def search_product(context, product):
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
#     sleep(6)  # wait for ads to disappear
#
#
# @then('Verify header is present')
# def verify_header_present(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[class*='UtilityHeaderContainer']")
#
#
# @then('Verify header has {number} links')
# def verify_header_present(context, number):
#     number = int(number)
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
#     # always return [].[WebElement1, WebElement2,WebElement2]
#     # find_elements() herzaman bisey doner ama find_element fail olur
#     # find element ve find_elements farki
#     # 1- birden fazla link doneceksen elements kullaniyor
#     # 2- element fail olur ama elements olmaz bise bulamazsa bos liste doner
#     assert len(links) == number, f'Expected {number} links,but got {len(links)}'

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(6)  # wait for ads to disappear
    print(product)
    context.app.main_page.search(product)

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()

@when('Click on cart icon')
def click_sign_in(context):
    context.driver.find_element(*CART_ICON).click()

@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.driver.find_element(*SIDE_MENU_SIGN_IN).click()


@then('Verify header is present')
def verify_header_preset(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    number = int(number)  # convert str to int
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'