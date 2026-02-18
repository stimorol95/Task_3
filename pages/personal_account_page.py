import allure
from pages.base_page import BasePage
from locators.locators import PersonalAccountPageLocators as PAPL

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по ссылке 'История заказов'")
    def click_order_history_link(self):
        self.click_element(PAPL.ORDER_HISTORY_LINK)
        return self

    @allure.step("Клик по кнопке 'Выход'")
    def click_logout_button(self):
        self.click_element(PAPL.LOGOUT_BUTTON)
        return self

    @allure.step("Проверка отображения страницы профиля")
    def is_profile_page_displayed(self):
        return self.is_element_displayed(PAPL.PROFILE_LINK)