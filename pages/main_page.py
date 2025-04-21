from pages.base_page import Page

class MainPage(Page):

    def open_target_main_page(self):
        self.open_url('https://www.target.com')
