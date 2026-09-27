
import time

from pages.home_page import HomePage
from pages.register_page import RegisterPage


def test_registration_required_field_validation(driver, base_url):
    """Submitting the registration form empty should show field warnings."""
    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.go_to_register()

    register_page = RegisterPage(driver)

    # Submit immediately without filling anything in.
    register_page.submit()

    warnings = register_page.get_field_warnings()
    assert len(warnings) > 0, (
        "Expected at least one validation warning when submitting the "
        "registration form with all required fields empty."
    )


def test_registration_with_placeholder_data(driver, base_url):
    """
    Fill the registration form with placeholder data and submit it.
    This is a workflow demonstration using fake placeholder details.
    """
    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.go_to_register()

    register_page = RegisterPage(driver)

    # Generate a unique placeholder email for each test run.
    unique_suffix = str(int(time.time()))
    placeholder_first_name = "Test"
    placeholder_last_name = "Automation"
    placeholder_email = f"test.automation.{unique_suffix}@example.com"
    placeholder_telephone = "9999999999"
    placeholder_password = "PlaceholderPass123!"

    register_page.fill_registration_form(
        first_name=placeholder_first_name,
        last_name=placeholder_last_name,
        email=placeholder_email,
        telephone=placeholder_telephone,
        password=placeholder_password,
    )

    register_page.agree_to_privacy_policy()
    register_page.submit()

    assert register_page.is_registration_successful(), (
        "Expected the account-created confirmation after registration."
    )


def test_registration_without_agreeing_to_privacy_policy(driver, base_url):
    """
    Filling the form correctly but not ticking the privacy policy
    checkbox should block registration with a warning message.
    """
    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.go_to_register()

    register_page = RegisterPage(driver)

    # Generate a unique placeholder email for this test run.
    unique_suffix = str(int(time.time()))

    register_page.fill_registration_form(
        first_name="Test",
        last_name="NoAgree",
        email=f"test.noagree.{unique_suffix}@example.com",
        telephone="9999999999",
        password="PlaceholderPass123!",
    )

    # Intentionally do not agree to the privacy policy.
    register_page.submit()

    alert_text = register_page.get_privacy_alert_text()
    assert alert_text != "", (
        "Expected a warning about the Privacy Policy not being agreed to."
    )