from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
COLOR_OPTIONS2 = (By.CSS_SELECTOR, "a[class*='styles__StyledBaseButtonInternal'] img")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(6)


@then('Verify user can click through {expected_colors}')
def click_and_verify_colors(context, expected_colors):
    #expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
    #expected_colors = []
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]  # 'Color\nBlack' => ['Color', 'Black']
        actual_colors.append(selected_color)
    print('Expected colors type:', expected_colors)
    print('Actual colors type:', actual_colors)
    assert list(expected_colors) in actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

