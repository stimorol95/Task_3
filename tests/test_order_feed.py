import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from api.user_api import create_user, delete_user

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_order_modal_appears(self, driver):
        main_page = MainPage(driver)
        order_feed_page = main_page.click_on_order_feed()
        order_feed_page.click_on_order()
        assert order_feed_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'")
    def test_user_orders_in_feed(self, driver, registered_user):
        main_page = MainPage(driver)
        order_feed_page = main_page.click_on_order_feed()
        orders = order_feed_page.get_all_orders_numbers()
        assert len(orders) > 0

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_completed_all_time_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        order_feed_page = main_page.click_on_order_feed()
        initial_value = int(order_feed_page.get_completed_counter_all_time())
        main_page.click_on_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_place_order_button()
        main_page.click_on_order_feed()
        new_value = int(order_feed_page.get_completed_counter_all_time())
        assert new_value > initial_value

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_completed_today_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        order_feed_page = main_page.click_on_order_feed()
        initial_today = int(order_feed_page.get_completed_counter_today())
        main_page.click_on_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_place_order_button()
        main_page.click_on_order_feed()
        new_today = int(order_feed_page.get_completed_counter_today())
        assert new_today > initial_today

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_work(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = main_page.click_login_button_on_main()
        main_page = login_page.login(registered_user['email'], registered_user['password'])
        main_page.add_ingredient_to_order()
        main_page.click_place_order_button()
        order_id = main_page.get_order_id_from_popup()
        order_feed_page = main_page.click_on_order_feed()
        orders_in_work = order_feed_page.get_orders_in_work()
        assert order_id in orders_in_work