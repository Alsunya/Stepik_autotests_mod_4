from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        btn.click()
