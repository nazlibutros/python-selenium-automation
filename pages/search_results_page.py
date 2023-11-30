from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")

    def verify_search_result(self, product):
        # search_results_header = self.find_element(*self.SEARCH_RESULT_TXT).text
        # assert product in search_results_header, \
        #     f'Expected text {product} not in {search_results_header}'
        self.verify_partial_text(product, *self.SEARCH_RESULT_TXT)

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def get_product_name(self):
        return self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME).text

    # def verify_search_url(self, expected_partial_url):
    #     # assert expected_keyword in self.driver.current_url, \
    #     #     f'Expected keyword: {expected_keyword} not in {self.driver.current_url}'
    #     self.verify_partial_url(expected_partial_url)
    #
    #  def click_add_to_cart(self):
    #      self.click(*self.ADD_TO_CART_BTN)

     #
     # def get_product_name(self):
     #     return self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME).text