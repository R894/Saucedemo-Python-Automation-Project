import os.path

import pytest_html
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
    request.cls.base_url = base_url
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    rep = outcome.get_result()
    extra = getattr(rep, "extra", [])
    if rep.when == 'call' and rep.failed:
        if 'setup' in item.fixturenames:
            web_driver = item.funcargs['setup']
    else:
        return
    report_directory = os.path.dirname(item.config.option.htmlpath)
    file_name = "screenshots/"+rep.nodeid.replace("::", "_") + ".png"
    destination_file = os.path.join(report_directory, file_name)
    web_driver.save_screenshot(destination_file)
    html = '<div><img src ="%s" alt="screenshot" style="width:300px;height=200px"' \
           'onclick="window.open(this.src)" align="right"/></div>'%file_name
    extra.append(pytest_html.extras.html(html))
    rep.extra = extra

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


def pytest_html_report_title(report):
    report.title = "Automation Report"
