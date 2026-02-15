from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators as RPL

class RecoveryPasswordPage(BasePage):
    def enter_email_and_click_recovery(self, email):
        self.send_keys_to_element(RPL.EMAIL_INPUT, email)
        self.click_element(RPL.RECOVERY_BUTTON)
        return self

    def click_show_hide_password_button(self):
        self.click_element(RPL.SHOW_HIDE_PASSWORD_BUTTON)
        return self

    def is_password_field_active(self):
        password_field = self.find_element(RPL.PASSWORD_INPUT)
        if password_field:
            class_attr = password_field.get_attribute("class")
            return "input_status_active" in class_attr
        return False

    def is_recovery_button_displayed(self):
        return self.is_element_displayed(RPL.RECOVERY_BUTTON)