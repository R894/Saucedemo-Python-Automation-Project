from selenium.webdriver.common.by import By

from Base.base_page import BasePage

class CheckoutOverview(BasePage):
    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver

    button_finish_id = "finish"
    button_cancel_id = "cancel"

    def get_finish_button(self):
        self.driver.find_element(By.ID, self.button_finish_id)

    def get_finish_button(self):
        self.driver.find_element(By.ID, self.button_cancel_id)