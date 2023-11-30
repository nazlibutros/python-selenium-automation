from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CartPage(Page):

    HEADER = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty_txt(self):
        # expected = 'Your cart is empty'
        # actual = self.find_element(*self.HEADER).text
        # assert expected == actual, f'{expected} not matched {actual}'
        self.verify_text('Your cart is empty', *self.HEADER)

    def verify_cart_item_amount(self, expected_amount):
        self.verify_partial_text(f'{expected_amount} item', *self.CART_SUMMARY)

    def verify_product_name(self, expected_name):
        self.verify_text(expected_name,*self.CART_ITEM_TITLE)

    def open_cart_page(self):
        self.open_url('https://www.target.com/cart')
