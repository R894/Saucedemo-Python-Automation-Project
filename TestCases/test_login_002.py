import time

import pytest

from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen


@pytest.mark.usefixtures("setup")
class Test_Login_002:
    logger = LogGen.loggen()

    def test_login_002(self):
        username = "standard_user"
        password = "ducks"
        lp = LoginPage(self.driver)
        lp.set_user_name(username)
        print(lp.get_username_textbox_text())
        assert True if lp.get_username_textbox_text() == username else False
        lp.set_password(password)
        assert True if lp.get_password_textbox_text() == password else False
        lp.click_login()
        time.sleep(2)
        print("wow printed" + lp.get_error_message_popup().text)
        assert True if "Epic sadface: Username and password do not match any user in this service" == \
                       lp.get_error_message_popup().text else False

