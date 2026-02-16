from pages.base_page import BasePage
from locators.locators import LoginPageLocators as LPL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_recovery_password_link(self):
        self.click_element(LPL.RECOVERY_PASSWORD_LINK)
        return self

    def login(self, email, password, retries=2):
        for attempt in range(retries):
            email_field = self.find_element(LPL.EMAIL_INPUT)
            email_field.clear()
            email_field.send_keys(email)

            password_field = self.find_element(LPL.PASSWORD_INPUT)
            password_field.clear()
            password_field.send_keys(password)

            self.click_element(LPL.LOGIN_BUTTON)

            try:
                WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(LPL.LOGIN_BUTTON)
                )
                return self
            except:
                if attempt == retries - 1:
                    raise
                self.driver.refresh()
                time.sleep(2)
        return self

    def is_login_button_displayed(self):
        return self.is_element_displayed(LPL.LOGIN_BUTTON)