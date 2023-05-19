import pytest

from Base.base_page import BasePage
from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
import time


@pytest.mark.usefixtures("setup")
class Test_AddToCart:
    logger = LogGen.loggen()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_001_add_to_cart(self):
        time.sleep(2)
        lp = LoginPage(self.driver)

        lp.set_user_name(self.username)
        lp.set_password(self.password)

        lp.click_login()

        hp = HomePage(self.driver)
        hp.add_item_to_cart(0)

        assert hp.get_item_count_in_cart() == 1

