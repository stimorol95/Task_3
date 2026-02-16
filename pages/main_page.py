import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.locators import MainPageLocators as MPL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_constructor(self):
        self.click_element(MPL.CONSTRUCTOR_LINK)
        return self

    def click_on_order_feed(self):
        self.click_element(MPL.ORDER_FEED_LINK)
        return self

    def click_on_personal_account(self):
        self.click_element(MPL.PERSONAL_ACCOUNT_LINK)
        return self 

    def click_on_ingredient(self):
        self.click_element(MPL.INGREDIENT)
        return self

    def close_modal_window(self):
        self.click_element(MPL.MODAL_CLOSE_BUTTON)
        return self

    def get_ingredient_counter(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        counters = ingredient.find_elements(*MPL.INGREDIENT_COUNTER)
        if counters:
            return int(counters[0].text)
        return 0

    def is_modal_window_displayed(self):
        return self.is_element_displayed(MPL.MODAL_WINDOW)

    def click_place_order_button(self):
        self.click_element(MPL.PLACE_ORDER_BUTTON)
        return self

    def get_order_id_from_popup(self):
        order_text = self.get_text_from_element(MPL.ORDER_ID_IN_MODAL)
        clean_number = order_text.replace('#', '').strip()
        return '0' + clean_number

    def click_login_button_on_main(self):
        self.click_element(MPL.LOGIN_BUTTON_ON_MAIN)
        return self

    def add_bun_to_constructor(self, bun_locator, position="top"):
        bun = self.find_element(bun_locator)
        if position == "top":
            target = self.find_element(MPL.BUN_ZONE_TOP)
        else:
            target = self.find_element(MPL.BUN_ZONE_BOTTOM)
        self._js_drag_and_drop(bun, target)
        return self

    def drag_ingredient_to_constructor(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        target = self.find_element(MPL.CONSTRUCTOR_BASKET)
        self._js_drag_and_drop(ingredient, target)
        return self

    def _js_drag_and_drop(self, source, target):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
        time.sleep(0.5)
        script = """
            const source = arguments[0];
            const target = arguments[1];
            
            // Создаём события перетаскивания
            const dataTransfer = new DataTransfer();
            
            // Запускаем события
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
        self.driver.execute_script(script, source, target)
        time.sleep(0.5)

    def close_modal_if_present(self, timeout=10):
        try:
            close_btn = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(MPL.MODAL_CLOSE_BUTTON)
            )
            self.driver.execute_script("arguments[0].click();", close_btn)
            
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(MPL.MODAL_WINDOW)
            )
            
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(MPL.MODAL_OVERLAY)
                )
            except:
                pass
                
            if 'firefox' in self.driver.capabilities['browserName'].lower():
                import time
                time.sleep(1)
                
        except TimeoutException:
            pass
        return self