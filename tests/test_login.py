from pages.login_page import LoginPage


def test_login_invalid_password(driver):
    """Try logging in with a valid username but an incorrect password."""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")

    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.get_error_message() == expected_error, "Error message did not match expected."


def test_login_invalid_username(driver):
    """Try logging in with an incorrect username and a valid password."""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "secret_sauce")

    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.get_error_message() == expected_error, "Error message did not match expected."


def test_login_empty_fields(driver):
    """Attempt to log in without entering any credentials."""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("", "")

    expected_error = "Epic sadface: Username is required"
    assert login_page.get_error_message() == expected_error, "Error message did not match expected."
