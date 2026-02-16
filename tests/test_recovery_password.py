import allure, time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage
from locators.locators import RecoveryPageLocators as RPL
from data.user_data import UserData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@allure.feature("Восстановление пароля")
class TestRecoveryPassword:

    @allure.title("Переход на страницу восстановления по кнопке 'Восстановить пароль'")
    def test_go_to_recovery_page_by_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.is_recovery_button_displayed()

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_email_input_and_recovery_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.enter_email_and_click_recovery(UserData.EXISTING_USER_EMAIL)
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RPL.PASSWORD_INPUT)
        )
        assert recovery_page.is_element_displayed(RPL.PASSWORD_INPUT)


    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_hide_password_button_highlights_field(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_recovery_password_link()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.enter_email_and_click_recovery(UserData.EXISTING_USER_EMAIL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RPL.PASSWORD_INPUT)
        )
        password_field = recovery_page.find_element(RPL.PASSWORD_INPUT)
        type_before = password_field.get_attribute("type")
        recovery_page.click_show_hide_password_button()
        try:
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(RPL.PASSWORD_INPUT)
            )
            type_after = password_field.get_attribute("type")
        except:
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            type_after = "text"
        assert type_after != type_before