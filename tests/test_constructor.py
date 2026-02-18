import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.locators import MainPageLocators as MPL

@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.click_on_constructor()
        assert main_page.is_text_present_on_page("Соберите бургер")

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        assert "feed" in main_page.get_current_url()

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_ingredient_modal_appears(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_for_visibility(MPL.MODAL_WINDOW)
        assert main_page.is_modal_window_displayed()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_for_visibility(MPL.MODAL_WINDOW)
        main_page.close_modal_window()
        main_page.wait_for_invisibility(MPL.MODAL_WINDOW)
        assert not main_page.is_modal_window_displayed()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер данного ингредиента")
    def test_ingredient_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        LoginPage(driver).login(registered_user['email'], registered_user['password'])
        main_page = MainPage(driver)
        meat_locator = MPL.MEAT_INGREDIENT
        initial_count = main_page.get_ingredient_counter(meat_locator)
        main_page.drag_ingredient_to_constructor(meat_locator)
        main_page.wait_for_counter_change(meat_locator, main_page.get_ingredient_counter, initial_count)
        new_count = main_page.get_ingredient_counter(meat_locator)
        assert new_count > initial_count

    @allure.title("Залогиненный пользователь может оформить заказ с булкой и мясом")
    def test_create_order_with_bun_and_meat(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        LoginPage(driver).login(registered_user['email'], registered_user['password'])
        main_page = MainPage(driver)
        main_page.add_bun_to_constructor(MPL.BUN_INGREDIENT, "top")
        main_page.drag_ingredient_to_constructor(MPL.MEAT_INGREDIENT)
        main_page.click_place_order_button()
        main_page.wait_for_visibility(MPL.ORDER_ID_IN_MODAL)
        order_id = main_page.get_order_id_from_popup()
        assert order_id.isdigit()