from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify search worked')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert 'coffee' in search_results_header, f'Expected text coffee not in {search_results_header}'


@then('Verify search result url')
def verify_search_url(context):
    assert 'coffee' in context.driver.current_url



@when('Click on cart icon')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify cart is empty message shown')
def verify_search_cart(context):
    search_results_header = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    print(search_results_header)
    assert 'Your cart is empty' in search_results_header, f'Expected text Your cart is empty not in {search_results_header}'


@when('Click Sign in')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(6)  # wait for ads to disappear


@then('From right side navigation menu, click Sign In')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify Sign In form opened')
def verify_search_signin(context):
    search_results_header = context.driver.find_element(By.XPATH, "//span[text() ='Sign into your Target account']").text
    print(search_results_header)
    assert 'Sign into your Target account' in search_results_header, f'Expected text Sign into your Target account not in {search_results_header}'

# "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa'