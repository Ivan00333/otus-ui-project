from playwright.sync_api import Page, TimeoutError, Response
from config.environment import host
from utils.logger import logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri: str) -> Response:
        url = f"{host.base_url}{uri}"
        logger.info(f"Opening URL: {url}")
        response = self.page.goto(url, wait_until="domcontentloaded")

        return response

    def click(self, locator: str) -> None:
        logger.info(f"Clicking element: {locator}")
        try:
            self.page.click(locator)
        except TimeoutError as e:
            logger.error(f"Timeout waiting to click {locator}: {e}", exc_info=True)
            raise

    def input(self, locator: str, data: str) -> None:
        logger.info(f"Filling element {locator} with data: '{data}'")
        try:
            self.page.locator(locator).fill(data)
        except TimeoutError as e:
            logger.error(f"Timeout waiting to fill {locator}: {e}", exc_info=True)
            raise

    def wait_for_element(self, locator: str, timeout: int = 12000) -> None:
        logger.info(f"Waiting for element {locator} (timeout={timeout}ms)")
        try:
            self.page.wait_for_selector(locator, timeout=timeout)
            logger.debug(f"Element appeared: {locator}")
        except TimeoutError as e:
            logger.error(f"Element {locator} did not appear in {timeout}ms: {e}", exc_info=True)
            raise

    def get_text(self, locator: str) -> str:
        logger.info(f"Getting text from element: {locator}")
        text = self.page.locator(locator).text_content()
        logger.debug(f"Text for {locator}: '{text}'")
        return text or ""

    def get_elements_text_list(self, locator: str) -> list[str]:
        logger.info(f"Getting inner texts from elements: {locator}")
        texts = self.page.locator(locator).all_inner_texts()
        logger.debug(f"Found texts: {texts}")
        return texts

    def click_element_by_index(self, locator: str, index: int) -> None:
        logger.info(f"Clicking element #{index} for locator: {locator}")
        try:
            self.page.locator(locator).nth(index).click()
        except TimeoutError as e:
            logger.error(f"Timeout clicking element #{index} ({locator}): {e}", exc_info=True)
            raise
