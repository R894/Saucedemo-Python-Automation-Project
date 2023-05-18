from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.base_page import BasePage


class HomePage(BasePage):
    # Locators
    button_shoppingcart_id = "shopping_cart_container"
    field_inventory_items_class = "inventory_item"
    button_add_to_cart_xpath = "add-to-cart-sauce-labs-backpack"
    button_burger_menu_button_css_selector = "#react-burger-menu-btn"
    button_logout_id = "logout_sidebar_link"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_shoppingcart_button(self):
        return self.driver.find_element(By.ID, self.button_shoppingcart_id)

    def get_burger_menu(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.button_burger_menu_button_css_selector)

    def get_logout_button(self):
        return self.driver.find_element(By.ID, self.button_logout_id)

    def click_burger_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.get_burger_menu())).click()

    def click_logout_button(self):
        logout_button = self.get_logout_button()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(logout_button))
        logout_button.click()

    def perform_logout_operation(self):
        self.click_burger_menu()
        self.click_logout_button()
