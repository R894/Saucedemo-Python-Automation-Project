from selenium.webdriver.common.by import By

from Base.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cart_items_css_selector = ".cart_item"
    cart_items_pricebar_css_selector = ".cart_item .item_pricebar"
    cart_items_name_css_selector = ".inventory_item_name"
    cart_items_button_css_selector = ".cart_item_label .btn"


    def get_cart_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_items_css_selector)

    def get_cart_item_pricebar_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_items_pricebar_css_selector).text

    def get_cart_item_pricebars_text(self):
        text_list = []
        for x in self.get_cart_item_pricebar_elements():
            text = x.text
            text_list.append(text)

        return text_list

    def get_cart_item_names(self):
        text_list = []

        for x in self.get_cart_item_pricebar_elements():
            text_list.append(self.get_cart_item_name(x))

        return text_list

    def get_cart_item_pricebar(self, item):
        return item.find_element(By.CSS_SELECTOR, self.cart_items_pricebar_css_selector)

    def get_cart_item_name(self, item):
        return item.find_element(By.CSS_SELECTOR, self.cart_items_name_css_selector).text
