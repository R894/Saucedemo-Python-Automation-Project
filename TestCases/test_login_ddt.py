import time

import pytest

from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities import XLUtils
import time


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class Test_002_DDT_Login:
    path = ".//TestData/logindata.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self):
        self.logger.info("*********** Test_002_DDT_Login ***************")
        self.logger.info("*********** Verifying login DDT test **************")

        self.rows = XLUtils.get_row_count(self.path, 'Sheet1')

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        results_list = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.read_data(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.read_data(self.path, 'Sheet1', r, 3)

            current_url = self.driver.current_url
            self.logger.info("********** Entering username " + self.user + " and password" + self.password + "**********")
            self.lp.set_user_name(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()

            if self.exp == "pass":
                if current_url != self.driver.current_url:

                    results_list.append("pass")
                else:
                    results_list.append("fail")
                self.hp.perform_logout_operation()
            else:
                if current_url == self.driver.current_url:
                    results_list.append("pass")
                else:
                    results_list.append("fail")
            time.sleep(5)

        if 'fail' in results_list:
            self.logger.error("********** test_login FAIL **********")
            assert False
        else:
            self.logger.info("********** test_login PASS **********")
            assert True




