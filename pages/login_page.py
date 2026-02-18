import allure
from pages.base_page import BasePage
from locators.locators import LoginPageLocators as LPL
from locators.locators import MainPageLocators as MPL

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_recovery_password_link(self):
        self.click_element(LPL.RECOVERY_PASSWORD_LINK)
        return self

    @allure.step("Вход в систему с email: {email}")
    def login(self, email, password):
        self.send_keys_to_element(LPL.EMAIL_INPUT, email)
        self.send_keys_to_element(LPL.PASSWORD_INPUT, password)
        self.click_element(LPL.LOGIN_BUTTON)
        self.wait_for_visibility(MPL.PLACE_ORDER_BUTTON)
        return self

    @allure.step("Проверка отображения кнопки входа")
    def is_login_button_displayed(self):
        return self.is_element_displayed(LPL.LOGIN_BUTTON)