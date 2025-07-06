# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def fill_text_input(self, selector, text):
        self.page.locator(selector).fill(text)

    def click_element(self, selector):
        self.page.locator(selector).click()

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def is_element_visible(self, selector):
        return self.page.locator(selector).is_visible()