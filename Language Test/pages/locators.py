from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_AREA = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_AREA = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name = "login_submit"]')
    EMAIL_REGISTRATION_AREA = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION_AREA = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD_AREA = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
