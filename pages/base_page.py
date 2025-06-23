from playwright.sync_api import Page, TimeoutError, Response
from config.environment import host


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri: str):
        return self.page.goto(f"{host.base_url}{uri}", wait_until="domcontentloaded")

    def click(self, locator):
        self.page.click(locator)

    def input(self, locator, data: str):
        self.page.locator(locator).fill(data)

    def get_text(self, locator) -> str:
        return self.page.locator(locator).text_content()

    def get_elements_text_list(self, locator):
        return self.page.locator(locator).all_inner_texts()

    def click_element_by_index(self, locator, index: int):
        self.page.locator(locator).nth(index).click()