# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# @given('Open Target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')
#
# @when('Search for tea')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)
#
# @then('Verify correct search results show')
# def verify_search_results(context):
#     actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
#     print('Actual Text: ', actual_text)
#     expected_text = 'tea'
#     assert expected_text in actual_text, f'error,text te not in {actual_text}'
#     print('Test passed')
#
# @when('Click on Cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#
#
# @then('Verify “Your cart is empty” message is shown')
# def verify_cart_empty_message(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg").text
#     assert expected_text in actual_text, f'error,text te not in {actual_text}'
#
# @when('Click Sign In')
# def click_sign_in(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
#     sleep(5)
#
# @when('From right side navigation menu, click Sign In')
# def click_nav_sign_in(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
#     sleep(5)
#
# @then('Verify Sign In form opened')
# def verify_sign_in_opened(context):
#     expected_text = 'Sign into your Target account'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']").text
#     assert expected_text in actual_text, f'error,text te not in {actual_text}'