import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from utils.logger import logger


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--h', default=True, help='Choose headless: True or False')
    parser.addoption('--slow', default=200, type=int, help='Choose slow_mo for robot action')

@pytest.fixture()
def browser(request) -> Page:
    pw = sync_playwright().start()

    browser_name = request.config.getoption("browser")
    headless   = str(request.config.getoption("h")).lower() in ("true", "1", "yes")
    slow_mo    = request.config.getoption("slow")

    launch_args = {
        "headless": headless,
        "slow_mo": slow_mo,
        "args": ["--start-maximized", "--start-fullscreen", "--window-size=1920,1080"]
    }

    if browser_name == "chrome":
        browser = pw.chromium.launch(**launch_args)
    elif browser_name == "firefox":
        browser = pw.firefox.launch(**launch_args)
    else:
        raise ValueError(f"Unknown browser: {browser_name}")

    context = browser.new_context(viewport=None)

    page = context.new_page()
    logger.info(f"Launch {browser_name}, headless={headless}")
    yield page

    context.close()
    browser.close()
    pw.stop()



