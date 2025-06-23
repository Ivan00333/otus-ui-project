import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--h', default=False, help='Choose headless: True or False')
    parser.addoption('--slow', default=200, help='Choose slow_mo for robot action')

@pytest.fixture(scope='class')
def browser(request) -> Page:
    playwright = sync_playwright().start()
    if request.config.getoption("browser") == "chrome":
        browser = playwright.chromium.launch(
            headless=str(request.config.getoption("h")).lower() in ("true", "1", "yes"),
            slow_mo=request.config.getoption("slow"),
            args=['--start-maximized']
        )
        context = browser.new_context()
        page = context.new_page()
    elif request.config.getoption("browser") == "firefox":
        browser = playwright.chromium.launch(
            headless=str(request.config.getoption("h")).lower() in ("true", "1", "yes"),
            slow_mo=request.config.getoption("slow"),
            args=['--start-maximized']
        )
        context = browser.new_context()
        page = context.new_page()

    yield page

    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()



