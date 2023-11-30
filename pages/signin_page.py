from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SigninPage(Page):
    HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data - test = '@web/AccountLink']")
    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")

    def verify_signin_form_opened(self):
        self.verify_text('Sign into your Target account', *self.HEADER)

    def click_terms_and_conditions(self):
        self.click(*self.TERMS_AND_CONDITIONS_LINK)
