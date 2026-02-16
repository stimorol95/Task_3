from pages.base_page import BasePage
from locators.locators import OrderFeedPageLocators as OFPL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_order(self):
        self.click_element(OFPL.ORDER_ITEM)
        return self

    def is_order_modal_displayed(self):
        return self.is_element_displayed(OFPL.ORDER_MODAL)

    def get_all_orders_numbers(self):
        elements = self.driver.find_elements(*OFPL.ORDER_NUMBERS)
        numbers = []
        for el in elements:
            text = el.text
            clean_text = text.replace('#', '').strip()
            numbers.append(clean_text)
        return numbers

    def get_completed_counter_all_time(self):
        return self.get_text_from_element(OFPL.COMPLETED_ALL_TIME_COUNTER)

    def get_completed_counter_today(self):
        return self.get_text_from_element(OFPL.COMPLETED_TODAY_COUNTER)

    def get_orders_in_work(self):
        elements = self.driver.find_elements(*OFPL.ORDERS_IN_WORK_LIST)
        return [el.text for el in elements]