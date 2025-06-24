import allure
from playwright.sync_api import Page
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from assertions.assertions import Assertions
from locators.auth_locators import AuthLocators
from config.auth_config import AuthConfig as login_data
from utils.logger import logger

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step("Open login page")
    def open_login_page(self):
        self.open("")

    @allure.step("Perform user login with default credentials")
    def user_login(self):
        logger.info("Input login")
        self.page.locator(AuthLocators.USERNAME_INPUT).fill(login_data.login)
        logger.info("Input password")
        self.page.locator(AuthLocators.PASSWORD_INPUT).fill(login_data.password)
        self.click(AuthLocators.LOGIN_BUTTON)
        self.assertions.check_url("inventory.html", "Wrong URL")

