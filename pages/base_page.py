from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    def send_keys_to_element(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator, time=10):
        return self.find_element(locator, time).text

    def is_element_displayed(self, locator, time=5):
        try:
            return self.find_element(locator, time).is_displayed()
        except TimeoutException:
            return False