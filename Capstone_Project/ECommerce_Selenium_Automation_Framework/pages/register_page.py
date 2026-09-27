from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class RegisterPage(BasePage):

    # Form locators
    FIRST_NAME_INPUT = (By.ID, "input-firstname")
    LAST_NAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")

    # Validation and result locators
    FIELD_WARNING = (By.CSS_SELECTOR, "div.text-danger")
    PRIVACY_ALERT = (By.CSS_SELECTOR, "div.alert.alert-danger")

    # The registration confirmation is shown in the main content area.
    SUCCESS_HEADING = (By.CSS_SELECTOR, "#content h1")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_registration_form(
        self,
        first_name,
        last_name,
        email,
        telephone,
        password
    ):
        """Fill all text fields in the registration form."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.TELEPHONE_INPUT, telephone)
        self.type_text(self.PASSWORD_INPUT, password)
        self.type_text(self.CONFIRM_PASSWORD_INPUT, password)

    def agree_to_privacy_policy(self):
        """Select the privacy policy checkbox if it is not already selected."""
        checkbox = self.driver.find_element(
            *self.PRIVACY_POLICY_CHECKBOX
        )

        if not checkbox.is_selected():
            checkbox.click()

    def submit(self):
        """Submit the registration form."""
        self.click(self.CONTINUE_BUTTON)

    def get_field_warnings(self):
        """Return visible field-validation warning messages."""
        elements = self.driver.find_elements(*self.FIELD_WARNING)

        return [
            element.text.strip()
            for element in elements
            if element.is_displayed() and element.text.strip()
        ]

    def get_privacy_alert_text(self):
        """Return the privacy-policy alert text, or an empty string."""
        elements = self.driver.find_elements(*self.PRIVACY_ALERT)

        for element in elements:
            if element.is_displayed():
                return element.text.strip()

        return ""

    def get_page_heading(self, timeout=10):
        """
        Wait for and return the heading in the main content area.

        This may be the account-created confirmation heading after
        successful registration, or a different heading if the form
        submission did not reach the expected result page.
        """
        heading = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SUCCESS_HEADING)
        )

        return heading.text.strip()

    def is_registration_successful(self, timeout=20):
        """
        Return True only if the expected account-created message appears.
        """
        try:
            heading = self.get_page_heading(timeout)
            return "Your Account Has Been Created" in heading
        except TimeoutException:
            return False