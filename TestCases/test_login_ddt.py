import time

import pytest
from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities import XLUtils
import time


@pytest.mark.regression
@pytest.mark.sanity
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

        self.logger.info(f"********** Entering username {user} and password {password} **********")
        if user is not None:
            self.lp.set_user_name(user)

        self.logger.info(f"********** Checking if {user} in textbox" + " **********")

        if user is not None:
            assert self.lp.get_username_textbox_text() == user
        else:
            assert self.lp.get_username_textbox_text() == ''

        if password is not None:
            self.lp.set_password(password)
        self.lp.click_login()

        # Asserts for a login that's expected to pass
        if exp == "pass":
            if current_url != self.driver.current_url:
                self.logger.info(f"********** {user} {password} pass *********")
                assert True
            else:
                self.logger.error(f"********** {user} {password} FAIL *********")
                self.hp.perform_logout_operation()
                time.sleep(5)
                assert False
        else:  # Asserts for a login that's expected to fail
            if current_url == self.driver.current_url:
                assert True if self.lp.get_error_message_popup().is_displayed() else False
                self.logger.info(f"********** {user} {password} pass *********")
            else:
                self.logger.error(f"********** {user} {password} FAIL *********")
                self.hp.perform_logout_operation()
                time.sleep(5)
                assert False
        time.sleep(5)




