from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    COST_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    COST_OF_BASKET_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    NAME_OF_PRODUCT_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
