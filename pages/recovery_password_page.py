from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators as RPL

class RecoveryPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email_and_click_recovery(self, email):
        self.send_keys_to_element(RPL.EMAIL_INPUT, email)
        self.click_element(RPL.RECOVERY_BUTTON)
        return self

    def click_show_hide_password_button(self):
        self.click_element(RPL.SHOW_HIDE_PASSWORD_BUTTON)
        return self

    def is_password_field_active(self):
        try:
            password_field = self.find_element(RPL.PASSWORD_INPUT, time=5)
            if password_field:
                class_attr = password_field.get_attribute("class")
                print(f"Password field classes: {class_attr}")
                active_classes = [
                    "input_status_active",
                    "input__placeholder-focused",
                    "input__textfield-focused"
                ]
                
                for active_class in active_classes:
                    if active_class in class_attr:
                        return True
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def is_recovery_button_displayed(self):
        return self.is_element_displayed(RPL.RECOVERY_BUTTON)