import allure, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from locators.locators import MainPageLocators as MPL, OrderFeedPageLocators as OFPL

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_order_modal_appears(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        login_page = LoginPage(driver)
        login_page.login(registered_user['email'], registered_user['password'])
        main_page = MainPage(driver)
        main_page.add_bun_to_constructor(MPL.BUN_INGREDIENT, "top")
        main_page.drag_ingredient_to_constructor(MPL.MEAT_INGREDIENT)
        main_page.click_place_order_button()
        main_page.close_modal_if_present()
        time.sleep(5)
        main_page.click_on_order_feed()
        time.sleep(5)
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(OFPL.ORDER_ITEM))
        order_feed_page.click_on_order()
        assert order_feed_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'")
    def test_user_orders_in_feed(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        login_page = LoginPage(driver)
        login_page.login(registered_user['email'], registered_user['password'])
        main_page = MainPage(driver)
        main_page.add_bun_to_constructor(MPL.BUN_INGREDIENT, "top")
        main_page.drag_ingredient_to_constructor(MPL.MEAT_INGREDIENT)
        main_page.click_place_order_button()
        time.sleep(4.75)
        order_id = main_page.get_order_id_from_popup()
        print(f"Original order ID: {order_id}")
        order_id_with_zeros = order_id.zfill(7)
        print(f"Order ID with zeros (7 digits): {order_id_with_zeros}")
        main_page.close_modal_if_present()
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MPL.ORDER_FEED_LINK)
        )
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(OFPL.ORDER_NUMBERS)
        )
        orders = order_feed_page.get_all_orders_numbers()
        print(f"Orders in feed: {orders}")
        assert order_id_with_zeros in orders, f"Order {order_id_with_zeros} not found in {orders}"

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_completed_all_time_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        login_page = LoginPage(driver)
        login_page.login(registered_user['email'], registered_user['password'])
        main_page = MainPage(driver)
        time.sleep(5)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(OFPL.COMPLETED_ALL_TIME_COUNTER)
        )
        initial_value = int(order_feed_page.get_completed_counter_all_time())
        main_page = MainPage(driver)
        main_page.click_on_constructor()
        main_page.add_bun_to_constructor(MPL.BUN_INGREDIENT, "top")
        main_page.drag_ingredient_to_constructor(MPL.MEAT_INGREDIENT)
        main_page.click_place_order_button()
        time.sleep(5)
        main_page.close_modal_if_present()
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(
            lambda d: int(order_feed_page.get_completed_counter_all_time()) > initial_value
        )
        new_value = int(order_feed_page.get_completed_counter_all_time())
        assert new_value > initial_value

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_completed_today_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        login_page = LoginPage(driver)
        login_page.login(registered_user['email'], registered_user['password'])
        main_page = MainPage(driver)
        time.sleep(5)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(OFPL.COMPLETED_TODAY_COUNTER)
        )
        initial_today = int(order_feed_page.get_completed_counter_today())
        main_page = MainPage(driver)
        main_page.click_on_constructor()
        main_page.add_bun_to_constructor(MPL.BUN_INGREDIENT, "top")
        main_page.drag_ingredient_to_constructor(MPL.MEAT_INGREDIENT)
        main_page.click_place_order_button()
        time.sleep(5)
        main_page.close_modal_if_present()
        time.sleep(5)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(
            lambda d: int(order_feed_page.get_completed_counter_today()) > initial_today
        )
        new_today = int(order_feed_page.get_completed_counter_today())
        assert new_today > initial_today

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_work(self, driver, registered_user):
        main_page = MainPage(driver)
        main_page.click_login_button_on_main()
        login_page = LoginPage(driver)
        login_page.login(registered_user['email'], registered_user['password'])
        main_page.add_bun_to_constructor(MPL.BUN_INGREDIENT, "top")
        main_page.drag_ingredient_to_constructor(MPL.MEAT_INGREDIENT)
        main_page.click_place_order_button()
        time.sleep(5)
        order_id = main_page.get_order_id_from_popup()
        main_page.close_modal_if_present()
        main_page.click_on_order_feed()
        time.sleep(5)
        order_feed_page = OrderFeedPage(driver)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(OFPL.ORDERS_IN_WORK_LIST)
        )
        orders_in_work = order_feed_page.get_orders_in_work()
        print(f"Orders in work: {orders_in_work}")
        assert order_id in orders_in_work