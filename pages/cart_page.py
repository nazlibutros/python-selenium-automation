from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')  # 'https://www.target.com/' + 'cart'