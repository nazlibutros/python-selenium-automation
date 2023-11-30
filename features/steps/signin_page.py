from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    context.app.signin_page.verify_signin_form_opened()
    # expected = 'Sign into your Target account'
    # actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
    # assert expected == actual, f'Expected {expected} did not match actual {actual}'


# @when('Click Sign in')
# def click_sign_in(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
#     sleep(6)  # wait for ads to disappear


@then('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.app.main_page.click_sign_in_from_nav()


# @then('Verify Sign In form opened')
# def verify_search_signin(context):
#     search_results_header = context.driver.find_element(By.XPATH,
#                                                         "//span[text() ='Sign into your Target account']").text
#     print(search_results_header)
#     assert 'Sign into your Target account' in search_results_header, f'Expected text Sign into your Target account not in {search_results_header}'
