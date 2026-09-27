from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//a[contains(@class,'dropdown-toggle') and contains(.,'My Account')]")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    LOGO = (By.CSS_SELECTOR, "#logo")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def load(self):
        """Open the home page."""
        self.open(self.base_url)

    def is_loaded(self):
        """Return True if a known home page element (the logo) is present."""
        return self.is_element_present(self.LOGO, timeout=10)

    def go_to_login(self):
        """Open the 'My Account' dropdown and click Login."""
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_LINK)

    def go_to_register(self):
        """Open the 'My Account' dropdown and click Register."""
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.REGISTER_LINK)

    def search_product(self, keyword):
        """Type a keyword into the top search bar and submit the search."""
        self.type_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
