import time

import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("*********** Test_001_Login **************")
        self.logger.info("*********** Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Swag Labs":
            assert True
            self.logger.info("*********** home page title test is passed **************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("*********** home page title test failed **************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("*********** Verifying login test **************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        current_url = self.driver.current_url

        self.logger.info("*********** ENTERING LOGIN CREDENTIALS **************")

        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.logger.info("*********** LOGGING IN **************")

        time.sleep(2)
        if current_url != self.driver.current_url:
            self.logger.info("********** test_login PASS **********")
            assert True
        else:
            self.logger.error("********** test_login FAIL **********")
            assert False
