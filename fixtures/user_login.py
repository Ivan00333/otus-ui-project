import pytest
from pages.login_page import LoginPage


@pytest.fixture()
def user_login(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.user_login()
