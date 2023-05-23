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
    cart_checkout_button_id = "checkout"

    def get_cart_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_items_css_selector)

    def get_checkout_button(self):
        self.driver.find_element(By.ID, self.cart_checkout_button_id)

    def get_cart_item_by_name(self, name):
        for x in self.get_cart_items():
            if name in x.text:
                return x
        return None

    def remove_item_from_cart(self, element):
        element.find_element(By.CSS_SELECTOR, "button").click()

    def get_cart_item_pricebar_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart_items_pricebar_css_selector)

    def get_cart_item_pricebars_text(self):
        text_list = []
        for x in self.get_cart_item_pricebar_elements():
            text = x.text
            text_list.append(text)

        return text_list

    def get_cart_item_names(self):
        text_list = []

        for x in self.get_cart_items():
            text_list.append(self.get_cart_item_name(x))

        return text_list

    def get_cart_item_pricebar(self, item):
        return item.find_element(By.CSS_SELECTOR, self.cart_items_pricebar_css_selector)

    def get_cart_item_name(self, item):
        return item.find_element(By.CSS_SELECTOR, self.cart_items_name_css_selector).text

    def check_if_item_in_cart(self, item_name):

        item_list = self.get_cart_item_names()
        for item in item_list:
            print(item)
        if item_name in item_list:
            return True

        return False
