from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        btn.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should dissapear"
