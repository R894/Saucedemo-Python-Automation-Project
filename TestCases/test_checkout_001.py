import pytest

from pageObjects.login_page import LoginPage
from utilities.read_properties import ReadConfig


@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.usefixtures("setup")
class Test_Checkout_001:
    user = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_checkout_001(self):
        lp = LoginPage(self.driver)
        lp.perform_login(self.user, self.password)