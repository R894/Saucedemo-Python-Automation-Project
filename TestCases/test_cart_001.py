import pytest

from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
import time


@pytest.mark.usefixtures("setup")
class Test_Cart_001:
    logger = LogGen.loggen()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_cart_001(self):

        lp = LoginPage(self.driver)
        lp.set_user_name(self.username)
        lp.set_password(self.password)
        lp.click_login()

        hp = HomePage(self.driver)
        item = hp.get_random_inventory_item(self.driver)
        name = hp.get_item_name(item)
        hp.add_item_to_cart(item)
        time.sleep(2)
        hp.get_shopping_cart_button().click()
        time.sleep(2)

