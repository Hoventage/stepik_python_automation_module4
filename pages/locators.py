from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.ID, 'login_link_inc')


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, 'login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, ".login_form [type='email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, ".login_form [type='password']")
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, ".login_form a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form [name='login_submit']")

    REGISTER_FORM = (By.CLASS_NAME, 'register_form')
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, ".register_form [type='email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, ".register_form [name='registration-password1']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, ".register_form [name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form [name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_NAME = (By.CSS_SELECTOR, "#messages strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info p strong')
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
