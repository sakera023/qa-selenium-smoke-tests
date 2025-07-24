import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com/signup")
    yield driver
    driver.quit()

def test_signup_form(driver):
    assert "Signup" in driver.title
    fields = ["username", "email", "password"]
    for name in fields:
        assert driver.find_element(By.NAME, name)
