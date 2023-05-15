import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


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

        if act_title == "sometitle":
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
        self.hp = HomePage(self.driver)

        self.hp.clickLogin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
