from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


# @then('Verify search worked for {product}')
# def verify_search(context, product):
#     search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
#     assert product in search_results_header, f'Expected text {product} not in {search_results_header}'


# @then('Verify {expected_keyword} in search result url')
# def verify_search_url(context, expected_keyword):
#     assert expected_keyword in context.driver.current_url, \
#         f'Expected {expected_keyword} not in {context.driver.current_url}'
#

@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
