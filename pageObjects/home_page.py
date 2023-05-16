from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    button_shoppingcart_id = "shopping_cart_container"
    field_inventory_items_class = "inventory_item"
    button_add_to_cart_xpath = "add-to-cart-sauce-labs-backpack"
    button_burger_menu_button_css_selector = "#react-burger-menu-btn"
    button_logout_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def click_burger_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_burger_menu_button_css_selector).click()

    def click_logout_button(self):
        logout_button = self.driver.find_element(By.ID, self.button_logout_id)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_logout_id)))
        logout_button.click()

    def perform_logout_operation(self):
        self.click_burger_menu()
        self.click_logout_button()
