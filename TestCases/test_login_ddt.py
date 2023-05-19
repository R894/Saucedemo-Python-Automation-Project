import time

import pytest
from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities import XLUtils
import time

from utilities.read_properties import ReadConfig


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class Test_002_DDT_Login:

    logger = LogGen.loggen()

    @pytest.mark.parametrize('user, password, exp', XLUtils.get_rows_as_list(".//TestData//logindata.xlsx", "Sheet1"))
    def test_login_ddt(self, user, password, exp):
        self.driver.get(self.base_url)
        self.logger.info("*********** Test_002_DDT_Login ***************")
        self.logger.info("*********** Verifying login DDT test **************")

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        current_url = self.driver.current_url
        self.logger.info("********** Entering username " + user + " and password" + password + "**********")
        self.lp.set_user_name(user)
        self.lp.set_password(password)
        self.lp.click_login()

        if exp == "pass":
            if current_url != self.driver.current_url:
                self.logger.info("********** "+user +password +" pass *********" )
                assert True
            else:
                self.logger.error("********** "+user +password +" pass *********" )
                self.hp.perform_logout_operation()
                time.sleep(5)
                assert False
        else:
            if current_url == self.driver.current_url:
                self.logger.info("********** " + user + password + " pass *********")
                assert True
            else:
                self.logger.error("********** " + user + password + " pass *********")
                self.hp.perform_logout_operation()
                time.sleep(5)
                assert False
        time.sleep(5)




