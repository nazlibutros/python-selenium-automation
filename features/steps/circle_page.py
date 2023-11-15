from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Circle')
def click_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()
    sleep(6)  # wait for ads to disappear


@then('Verify there are 5 benefit boxes')
def verify_search_signin(context):
    benefit_boxes = context.driver.find_elements(By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
    assert len(benefit_boxes) == 5, f'Expected 5 links,but got {len(benefit_boxes)}'
