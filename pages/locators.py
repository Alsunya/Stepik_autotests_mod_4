from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE =(By.CSS_SELECTOR, ".col-sm-6 .price_color")
    CART_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    
