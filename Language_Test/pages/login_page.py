from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        comperens = 'login' in get_url
        assert comperens == True, 'Не старница логина'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_AREA), 'Нет поля логина'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_AREA), 'Нет поля пароль'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Нет кнопки логина'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_AREA), "Нет поля Email"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_AREA), "Нет поля пароля в регистрации"
        assert self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD_AREA), "Нет поля повтора пароля"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Нет кнопки регистарции"