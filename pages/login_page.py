# pages/login_page.py
from pages.base_page import BasePage
from utils.config_reader import Config

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button =  "//button[@type='submit' and @class='radius']"
        self.success_message = "#flash.success"
        self.error_message = "#flash.error"
        self.logout_button = ".button.secondary"

    def goto_login_page(self):
        self.navigate(Config.BASE_URL)

    def login(self, username, password):
        self.fill_text_input(self.username_input, username)
        self.fill_text_input(self.password_input, password)
        self.click_element(self.login_button)

    def get_success_message(self):
        return self.get_text(self.success_message)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_login_successful(self):
        return self.is_element_visible(self.success_message)

    def logout(self):
        self.click_element(self.logout_button)