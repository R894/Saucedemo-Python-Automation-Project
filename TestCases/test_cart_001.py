import pytest
from selenium.webdriver.common.by import By

from pageObjects.cart_page import CartPage
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
        item = hp.get_random_inventory_item_index()
        name = hp.get_item_name(item)
        print(name)

        hp.add_item_index_to_cart(item)
        time.sleep(2)
        hp.get_shopping_cart_button().click()
        time.sleep(2)

        cart_page = CartPage(self.driver)

        time.sleep(2)

        assert cart_page.check_if_item_in_cart(name)

