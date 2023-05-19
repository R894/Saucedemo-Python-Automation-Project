from selenium.webdriver.common.by import By
from Base.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_username_textbox(self):
        return self.driver.find_element(By.ID, self.textbox_username_id)

    def set_user_name(self, username):
        username_field = self.get_username_textbox()
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

