from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_MAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_MAIL = (By.CSS_SELECTOR, 'id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_AGAIN = (By.CSS_SELECTOR, '#id_registration-password2')