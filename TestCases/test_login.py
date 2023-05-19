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
        assert act_title == "Swag Labs"

