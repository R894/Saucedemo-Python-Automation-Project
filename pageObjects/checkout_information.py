from selenium.webdriver.common.by import By

from Base.base_page import BasePage


class CheckoutInformation(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    text_field_first_name_id = "first-name"
    text_field_last_name_id = "last-name"
    text_field_postal_code_id = "postal-code"
    button_continue_id = "continue"
    button_cancel_id = "cancel"

    def get_first_name_text_field(self):
        self.driver.find_element(By.ID, self.text_field_first_name_id)

    def get_last_name_text_field(self):
        self.driver.find_element(By.ID, self.text_field_last_name_id)

    def get_postal_code_text_field(self):
        self.driver.find_element(By.ID, self.text_field_postal_code_id)

    def get_continue_button(self):
        self.driver.find_element(By.ID, self.button_continue_id)

    def get_cancel_button(self):
        self.driver.find_element(By.ID, self.button_cancel_id)

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.get_first_name_text_field().send_keys(first_name)
        self.get_last_name_text_field().send_keys(last_name)
        self.get_postal_code_text_field().send_keys(postal_code)