from pages.base_page import BasePage
from locators.locators import LoginPageLocators as LPL

class LoginPage(BasePage):
    def click_recovery_password_link(self):
        self.click_element(LPL.RECOVERY_PASSWORD_LINK)
        from pages.recovery_password_page import RecoveryPasswordPage  # локальный импорт
        return RecoveryPasswordPage(self.driver)

    def login(self, email, password):
        self.send_keys_to_element(LPL.EMAIL_INPUT, email)
        self.send_keys_to_element(LPL.PASSWORD_INPUT, password)
        self.click_element(LPL.LOGIN_BUTTON)
        from pages.main_page import MainPage  # локальный импорт
        return MainPage(self.driver)

    def is_login_button_displayed(self):
        return self.is_element_displayed(LPL.LOGIN_BUTTON)