import allure
from pages.login_page import LoginPage

@allure.feature("Login")
class TestLogin:

    @allure.story("Successful login with valid credentials")
    @allure.title("Test login")
    def test_login(self, browser):
        login_page = LoginPage(browser)
        with allure.step("Open login page"):
            login_page.open_login_page()
        with allure.step("Perform user login"):
            login_page.user_login()
