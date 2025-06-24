import allure
from playwright.sync_api import Page, expect
from config.environment import host
from pages.base_page import BasePage


class Assertions(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Check URL equals '{uri}'")
    def check_url(self, uri: str, msg: str):
        expect(self.page).to_have_url(f"{host.get_base_url}{uri}", timeout=10000), msg

    @allure.step("Verify element '{locator}' has text '{text}'")
    def have_text(self, locator, text: str, msg: str):
        elm = self.page.locator(locator)
        expect(elm).to_have_text(text), msg

    @allure.step("Check count of elements '{locator}' equals {expected_count}")
    def check_count_elements(self, locator, expected_count: int):
        actual_count = self.page.locator(locator).count()
        assert actual_count == expected_count, \
            f"Incorrect number of items: expected {expected_count}, found {actual_count}"

    @allure.step("Check presence of element '{locator}'")
    def check_presence(self, locator):
        elm = self.page.locator(locator)
        expect(elm).to_be_visible(visible=True, timeout=10000)
