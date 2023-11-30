from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGNIN_NAV = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test = '@web/AccountLink']")

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_for_element_click(*self.CART_ICON)

    def click_signin(self):
        self.wait_for_element_click(*self.SIGNIN_BTN)

    def click_sign_in_from_nav(self):
        self.wait_for_element_click(*self.SIGNIN_NAV)
