from playwright.sync_api import Page
from pages.base_page import BasePage
from assertions.assertions import Assertions
from locators.auth_locators import AuthLocators
from config.auth_config import AuthConfig as login_data


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def open_login_page(self):
        self.open("")

    def user_login(self):
        self.input(AuthLocators.USERNAME_INPUT, login_data.login)
        self.input(AuthLocators.PASSWORD_INPUT, login_data.password)
        self.click(AuthLocators.LOGIN_BUTTON)
        self.assertions.check_url("inventory.html", "Wrong URL")
