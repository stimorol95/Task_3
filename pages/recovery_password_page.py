import allure
from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators as RPL

class RecoveryPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ввод email и клик по кнопке 'Восстановить'")
    def enter_email_and_click_recovery(self, email):
        self.send_keys_to_element(RPL.EMAIL_INPUT, email)
        self.click_element(RPL.RECOVERY_BUTTON)
        self.wait_for_visibility(RPL.PASSWORD_INPUT)
        return self

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_password_button(self):
        self.click_element(RPL.SHOW_HIDE_PASSWORD_BUTTON)
        return self

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        field_type = self.get_element_attribute(RPL.PASSWORD_INPUT, "type")
        return field_type == "text"

    @allure.step("Проверка отображения кнопки восстановления")
    def is_recovery_button_displayed(self):
        return self.is_element_displayed(RPL.RECOVERY_BUTTON)