from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.read_properties import ReadConfig


@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager.install()))

    base_url = ReadConfig.getApplicationURL()
    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'SauceDemo'
