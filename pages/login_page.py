from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/ru/accounts/login/', 'login url is ' \
                                                                                                       'not correct '

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.is_element_present(*)