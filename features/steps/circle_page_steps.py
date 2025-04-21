from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CIRCLE_BENEFITS = (By.CSS_SELECTOR, "[class='cell-item-content']")

@given('Open target circle page')
def open_target_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(2)

@then('Verify at least {link_amount} benefit links shown')
def verify_benefit_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*CIRCLE_BENEFITS)
    print(links)
    assert len(links) >= link_amount, f'Expected {link_amount} links, but got {len(links)}'