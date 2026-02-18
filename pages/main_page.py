import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.locators import MainPageLocators as MPL
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по ссылке 'Конструктор'")
    def click_on_constructor(self):
        self.click_element(MPL.CONSTRUCTOR_LINK)
        return self

    @allure.step("Клик по ссылке 'Лента заказов'")
    def click_on_order_feed(self):
        self.click_element(MPL.ORDER_FEED_LINK)
        return self

    @allure.step("Клик по ссылке 'Личный кабинет'")
    def click_on_personal_account(self):
        self.click_element(MPL.PERSONAL_ACCOUNT_LINK)
        return self

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click_element(MPL.INGREDIENT)
        return self

    @allure.step("Закрытие модального окна")
    def close_modal_window(self):
        self.click_element(MPL.MODAL_CLOSE_BUTTON)
        return self

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        counters = ingredient.find_elements(*MPL.INGREDIENT_COUNTER)
        if counters:
            return int(counters[0].text)
        return 0

    @allure.step("Проверка отображения модального окна")
    def is_modal_window_displayed(self):
        return self.is_element_displayed(MPL.MODAL_WINDOW)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        self.click_element(MPL.PLACE_ORDER_BUTTON)
        return self

    @allure.step("Получение номера заказа из модального окна")
    def get_order_id_from_popup(self):
        order_text = self.get_text_from_element(MPL.ORDER_ID_IN_MODAL)
        clean_number = order_text.replace('#', '').strip()
        return clean_number.zfill(7)

    @allure.step("Клик по кнопке 'Войти в аккаунт' на главной")
    def click_login_button_on_main(self):
        self.click_element(MPL.LOGIN_BUTTON_ON_MAIN)
        return self

    @allure.step("Добавление булки в конструктор")
    def add_bun_to_constructor(self, bun_locator, position="top"):
        bun = self.find_element(bun_locator)
        if position == "top":
            target = self.find_element(MPL.BUN_ZONE_TOP)
        else:
            target = self.find_element(MPL.BUN_ZONE_BOTTOM)
        self._drag_and_drop(bun, target)
        return self

    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        target = self.find_element(MPL.CONSTRUCTOR_BASKET)
        self._drag_and_drop(ingredient, target)
        return self

    def _drag_and_drop(self, source, target):
        """Перетаскивание с JavaScript-эмуляцией для Firefox"""
        self.scroll_to_element(source)
        self.scroll_to_element(target)
        is_firefox = 'firefox' in self.driver.capabilities['browserName'].lower()
        if is_firefox:
            self._js_drag_and_drop(source, target)
        else:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source, target).perform()

    def _js_drag_and_drop(self, source, target):
        """JavaScript эмуляция drag-and-drop для Firefox"""
        script = """
            const source = arguments[0];
            const target = arguments[1];
            
            // Создаём событие с dataTransfer
            const dataTransfer = new DataTransfer();
            
            // Запускаем события перетаскивания
            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
            
            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
            
            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """
        self.execute_script(script, source, target)

    @allure.step("Закрытие модального окна если оно есть")
    def close_modal_if_present(self, timeout=10):
        """Закрывает модальное окно и ждёт полного исчезновения overlay."""
        try:
            close_btn = self.find_element(MPL.MODAL_CLOSE_BUTTON, timeout)
            self.execute_script("arguments[0].click();", close_btn)
            self.wait_for_invisibility(MPL.MODAL_WINDOW, timeout)
            try:
                self.wait_for_invisibility(MPL.MODAL_OVERLAY, timeout)
            except:
                pass
            self.execute_script("""
                var overlays = document.querySelectorAll('[class*="Modal_modal_overlay"]');
                overlays.forEach(function(el) { el.remove(); });
            """)
            self.wait_for_clickable(MPL.ORDER_FEED_LINK, timeout)
        except Exception as e:
            self.execute_script("""
                var overlays = document.querySelectorAll('[class*="Modal_modal_overlay"]');
                overlays.forEach(function(el) { el.remove(); });
            """)
        return self