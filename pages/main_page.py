from pages.base_page import BasePage
from locators.locators import MainPageLocators as MPL

class MainPage(BasePage):
    def click_on_constructor(self):
        self.click_element(MPL.CONSTRUCTOR_LINK)
        return self

    def click_on_order_feed(self):
        self.click_element(MPL.ORDER_FEED_LINK)
        from pages.order_feed_page import OrderFeedPage  # локальный импорт
        return OrderFeedPage(self.driver)

    def click_on_personal_account(self):
        self.click_element(MPL.PERSONAL_ACCOUNT_LINK)
        from pages.login_page import LoginPage  # локальный импорт
        return LoginPage(self.driver)

    def click_on_ingredient(self):
        self.click_element(MPL.INGREDIENT)
        return self

    def close_modal_window(self):
        self.click_element(MPL.MODAL_CLOSE_BUTTON)
        return self

    def add_ingredient_to_order(self):
        self.click_on_ingredient()
        return self

    def get_ingredient_counter_value(self):
        counter = self.find_element(MPL.INGREDIENT_COUNTER)
        return int(counter.text) if counter and counter.text.isdigit() else 0

    def is_modal_window_displayed(self):
        return self.is_element_displayed(MPL.MODAL_WINDOW)

    def click_place_order_button(self):
        self.click_element(MPL.PLACE_ORDER_BUTTON)
        return self

    def get_order_id_from_popup(self):
        return self.get_text_from_element(MPL.ORDER_ID_IN_MODAL)

    def click_login_button_on_main(self):
        self.click_element(MPL.LOGIN_BUTTON_ON_MAIN)
        from pages.login_page import LoginPage  # локальный импорт
        return LoginPage(self.driver)