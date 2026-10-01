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


def test_login_page(driver):
    load_html(
        driver,
        "<title>Login</title>"
        '<input name="username">'
        '<input name="password" type="password">'
        '<button id="login">Log in</button>',
    )

    assert "Login" in driver.title
    assert driver.find_element(By.NAME, "username").is_displayed()
    assert driver.find_element(By.NAME, "password").is_displayed()
    assert driver.find_element(By.ID, "login").is_displayed()
