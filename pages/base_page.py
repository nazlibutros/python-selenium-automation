class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text} did not match actual {actual_text}'
