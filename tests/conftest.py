import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    """Initialize WebDriver before each test and close it after."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    time.sleep(4)  # Wait 4 seconds before closing to see tests execution on UI
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    """Log in as 'standard_user' before each test that requires authentication."""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Login failed."
    return driver
