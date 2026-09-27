from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
  
    ERROR_ALERT = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        """Fill in the login form and submit it."""
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """
        Return the text of the login error alert if it appears, otherwise
        return an empty string. Does not raise if the alert never shows up.
        """
        if self.is_element_present(self.ERROR_ALERT, timeout=10):
            return self.get_text(self.ERROR_ALERT)
        return ""
