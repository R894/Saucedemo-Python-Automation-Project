import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.base_page import BasePage


class HomePage(BasePage):
    # Locators
    button_shoppingcart_id = "shopping_cart_container"
    field_inventory_items_class = "inventory_item"
    button_add_to_cart_xpath = "//*[contains(@id, 'add-to-cart-')]"
    button_remove_from_cart_xpath = "//*[contains(@id, 'add-to-cart-')]"
    button_burger_menu_button_css_selector = "#react-burger-menu-btn"
    icon_shopping_cart_number_css_selector = ".shopping_cart_badge"
    button_logout_id = "logout_sidebar_link"
    text_inventory_item_names_css_selector = ".inventory_item_name"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Get Basic Elements
    def get_shoppingcart_button(self):
        return self.driver.find_element(By.ID, self.button_shoppingcart_id)

    def get_burger_menu(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.button_burger_menu_button_css_selector)

    def get_logout_button(self):
        return self.driver.find_element(By.ID, self.button_logout_id)

    def get_shopping_cart_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.icon_shopping_cart_number_css_selector)

    def get_shopping_item_list_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, self.field_inventory_items_class)

    def get_item_count_in_cart(self):
        return int(self.get_shopping_cart_icon().text)

    def get_item_name(self, driver):
        driver.find_element(By.CSS_SELECTOR, self.text_inventory_item_names_css_selector)

    # Page Functions

    def click_burger_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.get_burger_menu())).click()

    def click_logout_button(self):
        logout_button = self.get_logout_button()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(logout_button))
        logout_button.click()

    def add_item_to_cart(self, item_index):
        item = self.get_shopping_item_list_elements()[item_index]
        item.find_element(By.XPATH, self.button_add_to_cart_xpath).click()

    def perform_logout_operation(self):
        self.click_burger_menu()
        self.click_logout_button()

    def get_shopping_item_list_count(self):
        return len(self.get_shopping_item_list_elements())

    def get_inventory_item(self, index):
        return self.get_shopping_item_list_elements()[index]

    def get_random_inventory_item(self, driver):
        list_count = self.get_shopping_item_list_count()
        random_item_index = random.randint(0, list_count)

        return self.get_inventory_item(random_item_index)

