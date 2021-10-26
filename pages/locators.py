from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


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
