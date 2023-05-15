import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/logindata.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_Login ***************")
        self.logger.info("*********** Verifying login DDT test **************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        self.hp.clickLogin()

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1',r,3)

            self.lp.setUserName(self.user)
            time.sleep(2)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(5)

            if self.exp == "pass":
                self.hp.performLogout()

            time.sleep(5)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
