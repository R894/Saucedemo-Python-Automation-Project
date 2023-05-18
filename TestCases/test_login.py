import time

import pytest
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


@pytest.mark.usefixtures("setup")
class Test_001_Login:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self):

        self.logger.info("*********** Test_001_Login **************")
        self.logger.info("*********** Verifying Home Page Title **************")
        time.sleep(2)
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
