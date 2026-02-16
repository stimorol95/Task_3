from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Конструктор" в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@href, '/')]")
    # Кнопка "Лента заказов" в шапке
    ORDER_FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]")
    # Кнопка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    # Первый ингредиент в списке (булка)
    INGREDIENT = (By.XPATH, "(//a[contains(@href, '/ingredient')])[1]")
    # Счётчик ингредиента (родительский элемент для конкретного ингредиента)
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    # Активное модальное окно
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]")
    # Кнопка закрытия модального окна (крестик)
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Номер заказа в модалке после оформления
    ORDER_ID_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")
    # Кнопка "Войти в аккаунт" на главной (если пользователь неавторизован)
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
     # Контейнер для ингредиентов (корзина)
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'mt-25')]")
    # Зона для верхней булки
    BUN_ZONE_TOP = (By.XPATH, "//*[contains(text(),'Перетяните булочку сюда (верх)')]/..")
    # Зона для нижней булки
    BUN_ZONE_BOTTOM = (By.XPATH, "//*[contains(text(),'Перетяните булочку сюда (низ)')]/..")
    # Конкретные ингредиенты для тестов
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@href, '/ingredient')])[1]")  # Первая булка
    MEAT_INGREDIENT = (By.XPATH, "(//a[contains(@href, '/ingredient')])[3]")  # Первая начинка/мясо  

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Восстановить пароль"
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class RecoveryPageLocators:
    # Поле ввода email на странице восстановления
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    # Кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Иконка "показать/скрыть пароль" (глазик)
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    # Поле ввода нового пароля
    PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_type_password')]")
    # Кнопка "Сохранить" (после ввода нового пароля)
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Сохранить']")

class PersonalAccountPageLocators:
    # Ссылка "История заказов" в личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Ссылка "Профиль" (для проверки, что мы в ЛК)
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")

class OrderFeedPageLocators:
    # Элемент заказа в ленте (первый)
    ORDER_ITEM = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]")
    # Модальное окно с деталями заказа
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]")
    # Номера заказов в ленте (элементы с номером)
    ORDER_NUMBERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]")
    # Счётчик "Выполнено за всё время"
    COMPLETED_ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # Счётчик "Выполнено за сегодня"
    COMPLETED_TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Список заказов в работе (номера)
    ORDERS_IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    # Крестик закрытия модального окна (добавим, если нужен)
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    # Перекрытие экрана
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
