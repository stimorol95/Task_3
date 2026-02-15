import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from api.user_api import create_user, delete_user

@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет по клику на кнопку (авторизованный пользователь)")
    def test_go_to_personal_account(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        main_page.click_on_personal_account()
        account_page = PersonalAccountPage(driver)
        assert account_page.is_profile_page_displayed()

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        main_page.click_on_personal_account()
        account_page = PersonalAccountPage(driver)
        account_page.click_order_history_link()
        assert "order-history" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        main_page.click_on_personal_account()
        account_page = PersonalAccountPage(driver)
        login_page = account_page.click_logout_button()
        assert login_page.is_login_button_displayed()