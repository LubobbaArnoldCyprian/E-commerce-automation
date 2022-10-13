from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(6)
    driver.maximize_window()
    return driver

# This will get the value from CLI/hook
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to set up method
    return request.config.getoption("--browser")