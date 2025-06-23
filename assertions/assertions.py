from playwright.sync_api import Page, expect
from config.environment import host
from pages.base_page import BasePage


class Assertions(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def check_url(self, uri: str, msg :str):
        expect(self.page).to_have_url(f"{host.get_base_url}{uri}", timeout=10000), msg

    def have_text(self, locator, text: str, msg: str):
        locator = self.page.locator(locator)
        expect(locator).to_have_text(text), msg

    def check_count_elements(self, locator, expected_count: int):
        actual_count = self.page.locator(locator).count()

        assert actual_count == expected_count, \
            f"Incorrect number of items: expected {expected_count}, found {actual_count}"

    def check_presence(self, locator):
        locator = self.page.locator(locator)
        expect(locator).to_be_visible(visible=True, timeout=10000)
