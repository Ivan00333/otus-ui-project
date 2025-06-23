from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        login_page.user_login()