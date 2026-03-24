from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def test_valid_login_redirects_to_inventory():
    driver = create_driver()
    page = LoginPage(driver)
    try:
        page.open()
        page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url
    finally:
        driver.quit()


def test_invalid_login_shows_error():
    driver = create_driver()
    page = LoginPage(driver)
    try:
        page.open()
        page.login("standard_user", "wrong_password")
        assert "Epic sadface" in page.get_error_text()
    finally:
        driver.quit()
