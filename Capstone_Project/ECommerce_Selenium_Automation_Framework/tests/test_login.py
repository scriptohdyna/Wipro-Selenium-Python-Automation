
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config_reader import get_config


def test_invalid_login_shows_error_message(driver, base_url):
    """Verify that invalid placeholder credentials are rejected."""
    config = get_config()
    invalid_email = config.get("credentials", "invalid_email")
    invalid_password = config.get("credentials", "invalid_password")

    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.go_to_login()

    login_page = LoginPage(driver)
    login_page.login(invalid_email, invalid_password)

    error_message = login_page.get_error_message()
    assert error_message != "", (
        "Expected an error message after an invalid login attempt."
    )
    assert "warning" in error_message.lower() or "no match" in error_message.lower(), (
        f"Expected the error text to indicate the login failed, got: '{error_message}'"
    )


    current_url = login_page.get_current_url()
    assert "account/login" in current_url, (
        "Expected to remain on the login page after a failed login attempt, "
        f"but the current URL was: {current_url}"
    )
