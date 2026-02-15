from pages.base_page import BasePage
from locators.locators import PersonalAccountPageLocators as PAPL

class PersonalAccountPage(BasePage):
    def click_order_history_link(self):
        self.click_element(PAPL.ORDER_HISTORY_LINK)
        return self

    def click_logout_button(self):
        self.click_element(PAPL.LOGOUT_BUTTON)
        from pages.login_page import LoginPage  # локальный импорт
        return LoginPage(self.driver)

    def is_profile_page_displayed(self):
        return self.is_element_displayed(PAPL.PROFILE_LINK)