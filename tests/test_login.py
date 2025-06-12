import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_config import config
from datetime import datetime
import os

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(filename)

@allure.title("Valid Login Test")
@allure.description("Test if user can log in with valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.BASE_URL)

    try:
        driver.find_element(By.ID, "username").send_keys(config.LOGIN_EMAIL)
        driver.find_element(By.ID, "password").send_keys(config.LOGIN_PASSWORD)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        success_message = driver.find_element(By.TAG_NAME, "h1").text
        assert "Logged In Successfully" in success_message
        take_screenshot(driver, "login_success")
    except Exception as e:
        take_screenshot(driver, "login_failed")
        raise e
    finally:
        driver.quit()