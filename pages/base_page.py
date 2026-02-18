from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.locators import MainPageLocators as MPL
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            f"Элемент {locator} не найден за {time} секунд"
        )

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            f"Элемент {locator} не кликабелен за {time} секунд"
        )
        element.click()

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def send_keys_to_element(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента {locator}")
    def get_text_from_element(self, locator, time=10):
        return self.find_element(locator, time).text

    @allure.step("Проверка отображения элемента {locator}")
    def is_element_displayed(self, locator, time=5):
        try:
            return self.find_element(locator, time).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            f"Элемент {locator} не видим за {time} секунд"
        )

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            f"Элемент {locator} не кликабелен за {time} секунд"
        )

    @allure.step("Ожидание невидимости элемента {locator}")
    def wait_for_invisibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator),
            f"Элемент {locator} все еще видим за {time} секунд"
        )

    @allure.step("Ожидание изменения текста элемента")
    def wait_for_text_change(self, locator, old_text, time=10):
        def text_changed(driver):
            current_text = self.get_text_from_element(locator, 1)
            return current_text != old_text
        return WebDriverWait(self.driver, time).until(
            text_changed,
            f"Текст элемента {locator} не изменился за {time} секунд"
        )

    @allure.step("Ожидание изменения значения счетчика")
    def wait_for_counter_change(self, locator, get_counter_func, initial_value, time=10):
        def counter_changed(driver):
            return get_counter_func(locator) != initial_value
        return WebDriverWait(self.driver, time).until(
            counter_changed,
            f"Счетчик {locator} не изменился за {time} секунд"
        )

    @allure.step("Получение атрибута {attribute} элемента {locator}")
    def get_element_attribute(self, locator, attribute, time=10):
        element = self.find_element(locator, time)
        return element.get_attribute(attribute)

    @allure.step("Проверка наличия текста на странице")
    def is_text_present_on_page(self, text):
        return text in self.driver.page_source

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Выполнение JavaScript скрипта")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element):
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Ожидание, что текст элемента {locator} не равен {text}")
    def wait_for_element_text_not_equal(self, locator, text, time=10):
        def text_not_equal(driver):
            element_text = self.get_text_from_element(locator, 1)
            return element_text != text
        return WebDriverWait(self.driver, time).until(
            text_not_equal,
            f"Текст элемента {locator} все еще равен '{text}' через {time} секунд")    
    
    @allure.step("Ожидание стабильности страницы (исчезновение overlay)")
    def wait_for_page_stability(self, timeout=5):
        """Ожидает исчезновения всех overlay элементов."""
        try:
            self.wait_for_invisibility(MPL.MODAL_OVERLAY, timeout)
        except:
            pass
        return self