from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    button_login_id = "loginAnchor"
    button_user_dropdown_xpath = "(//div[@id='registered-user'])[1]"
    button_logout_xpath = "//form[@action='/j_spring_security_logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def clickUserDropdown(self):
        self.driver.find_element(By.XPATH, self.button_user_dropdown_xpath);

    def performLogout(self):
        self.clickUserDropdown()
        self.clickLogout()