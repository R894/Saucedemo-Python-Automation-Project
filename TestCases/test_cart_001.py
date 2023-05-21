import pytest

from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig


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
        hp.get_item_count_in_cart()
        # still incomplete

