import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import get_config, get_base_url, get_bool, get_int
from utils.screenshot import take_screenshot


@pytest.fixture
def base_url():
    return get_base_url()


@pytest.fixture
def driver():
    config = get_config()

    options = Options()
    if get_bool("browser", "headless", fallback=False):
        options.add_argument("--headless=new")

    width = get_int("browser", "window_width", fallback=1366)
    height = get_int("browser", "window_height", fallback=768)
    options.add_argument(f"--window-size={width},{height}")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(get_int("browser", "implicit_wait", fallback=5))

    yield chrome_driver
    chrome_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture is not None:
            try:
                take_screenshot(driver_fixture, name=item.name)
            except Exception:
                pass
