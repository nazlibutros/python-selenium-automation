from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SigninPage(Page):

    HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data - test = '@web/AccountLink']")

    def verify_signin_form_opened(self):
        self.verify_text('Sign into your Target account', *self.HEADER)

