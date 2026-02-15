import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.click_on_constructor()
        assert "Соберите бургер" in driver.page_source

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        assert "feed" in driver.current_url

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_ingredient_modal_appears(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.is_modal_window_displayed()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_modal_window()
        assert not main_page.is_modal_window_displayed()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        initial_count = main_page.get_ingredient_counter_value()
        main_page.add_ingredient_to_order()
        new_count = main_page.get_ingredient_counter_value()
        assert new_count > initial_count

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        main_page.add_ingredient_to_order()
        main_page.click_place_order_button()
        order_id = main_page.get_order_id_from_popup()
        assert order_id.isdigit()