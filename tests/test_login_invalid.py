import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from test_config import config

def test_invalid_login(setup_browser):
    driver = setup_browser
    driver.get(config["site"])
    time.sleep(2)

    # Input invalid credentials
    driver.find_element(By.NAME, "email").send_keys("invalid@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

    time.sleep(3)
    assert "Login failed" in driver.page_source or "invalid" in driver.page_source.lower()