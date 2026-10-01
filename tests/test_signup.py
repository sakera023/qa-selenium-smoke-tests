import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def load_html(driver, html):
    driver.get("data:text/html;charset=utf-8," + html)


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_signup_form(driver):
    load_html(
        driver,
        "<title>Signup</title>"
        '<input name="username">'
        '<input name="email" type="email">'
        '<input name="password" type="password">',
    )

    assert "Signup" in driver.title
    for name in ("username", "email", "password"):
        assert driver.find_element(By.NAME, name).is_displayed()
