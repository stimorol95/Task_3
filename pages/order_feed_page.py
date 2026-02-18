import allure
from pages.base_page import BasePage
from locators.locators import OrderFeedPageLocators as OFPL
from selenium.webdriver.support.ui import WebDriverWait

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по заказу")
    def click_on_order(self):
        self.click_element(OFPL.ORDER_ITEM)
        return self

    @allure.step("Проверка отображения модального окна заказа")
    def is_order_modal_displayed(self):
        return self.is_element_displayed(OFPL.ORDER_MODAL)

    @allure.step("Получение всех номеров заказов из ленты")
    def get_all_orders_numbers(self):
        """Возвращает список номеров заказов из ленты (не из раздела 'В работе')."""
        elements = self.driver.find_elements(*OFPL.ORDER_NUMBERS)
        numbers = []
        for el in elements:
            text = el.text.strip()
            if text and text.isdigit():  # Берём только цифры
                numbers.append(text)
        return numbers

    @allure.step("Получение счетчика 'Выполнено за всё время'")
    def get_completed_counter_all_time(self):
        return self.get_text_from_element(OFPL.COMPLETED_ALL_TIME_COUNTER)

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_completed_counter_today(self):
        return self.get_text_from_element(OFPL.COMPLETED_TODAY_COUNTER)

    @allure.step("Ожидание появления заказов в разделе 'В работе'")
    def wait_for_orders_in_work_not_empty(self, time=15):
        """Ожидает, что в разделе 'В работе' появятся заказы."""
        def orders_not_empty(driver):
            orders = self.get_orders_in_work()
            return len(orders) > 0 and orders[0] != "Все текущие заказы готовы!"
        
        return WebDriverWait(self.driver, time).until(
            orders_not_empty,
            f"Заказы не появились в разделе 'В работе' за {time} секунд"
        )
    
    @allure.step("Получение списка заказов в работе")
    def get_orders_in_work(self):
        """Возвращает список номеров заказов в работе."""
        elements = self.driver.find_elements(*OFPL.ORDERS_IN_WORK_LIST)
        orders = []
        for el in elements:
            text = el.text.strip()
            if text and text != "Все текущие заказы готовы!":
                orders.append(text)
        return orders