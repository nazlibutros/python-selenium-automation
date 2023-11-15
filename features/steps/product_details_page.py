from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
COLOR_OPTIONS2 = (By.CSS_SELECTOR, "a[class*='styles__StyledBaseButtonInternal'] img")


@given('Open target product A-88062531 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-88062531')
    sleep(6)


@given('Open target product A-89191279 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-89191279')
    sleep(6)


@then('Verify user can click through colors1')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[
            1]  # 'Color\nBlack' => ['Color', 'Black']
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

    then('Verify user can click through colors1')


@then('Verify user can click through colors2')
def click_and_verify_colors2(context):
    expected_colors2 = ['Black', 'Green', 'Oatmeal', 'Red']
    actual_colors2 = []

    colors = context.driver.find_elements(*COLOR_OPTIONS2)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[
            1]  # 'Color\nBlack' => ['Color', 'Black']
        actual_colors2.append(selected_color)

    assert expected_colors2 == actual_colors2, f'Expected {expected_colors2} did not match actual {actual_colors2}'
