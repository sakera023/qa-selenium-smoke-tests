import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    yield driver
    driver.quit()

def test_login_page(driver):
    assert "Login" in driver.title
    username_box = driver.find_element(By.NAME, "username")
    password_box = driver.find_element(By.NAME, "password")
    login_btn = driver.find_element(By.ID, "login")
    assert username_box and password_box and login_btn
