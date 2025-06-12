import pytest
from selenium import webdriver

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Change to your login page URL
    yield driver
    driver.quit()