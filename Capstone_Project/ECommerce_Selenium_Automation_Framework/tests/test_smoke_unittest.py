import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from utils.config_reader import get_base_url, get_bool, get_int


class SmokeTestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = None

        options = Options()
        if get_bool("browser", "headless", fallback=False):
            options.add_argument("--headless=new")

        width = get_int("browser", "window_width", fallback=1366)
        height = get_int("browser", "window_height", fallback=768)
        options.add_argument(f"--window-size={width},{height}")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(
            get_int("browser", "implicit_wait", fallback=5)
        )
        self.base_url = get_base_url()

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_home_page_loads(self):
        home_page = HomePage(self.driver, self.base_url)
        home_page.load()

        self.assertTrue(
            home_page.is_loaded(),
            "Expected the home page logo element to be present after loading the site.",
        )
        self.assertIn(
            "tutorialsninja",
            home_page.get_current_url().lower(),
            "Expected the current URL to point to the tutorialsninja demo site.",
        )


if __name__ == "__main__":
    unittest.main()