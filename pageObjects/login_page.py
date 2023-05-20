from selenium.webdriver.common.by import By
from Base.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    popup_error_message_css_selector = "h3[data-test='error']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_username_textbox(self):
        return self.driver.find_element(By.ID, self.textbox_username_id)

    def get_password_textbox(self):
        return self.driver.find_element(By.ID, self.textbox_password_id)

    def get_error_message_popup(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.popup_error_message_css_selector)

    def get_error_message_popup_text(self):
        self.get_error_message_popup().get_attribute("value")

    def get_username_textbox_text(self):
        return self.get_username_textbox().get_attribute("value")

    def get_password_textbox_text(self):
        return self.get_password_textbox().get_attribute("value")

    def set_user_name(self, username):
        username_field = self.get_username_textbox()
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        password_textbox = self.get_password_textbox()
        password_textbox.clear()
        password_textbox.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

