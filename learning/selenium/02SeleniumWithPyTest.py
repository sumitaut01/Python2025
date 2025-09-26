import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("ChatGPT Selenium Python")
    search.submit()
    assert "ChatGPT" in driver.title
