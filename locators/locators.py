from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Конструктор" в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    # Кнопка "Лента заказов" в шапке
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента заказов']")
    # Кнопка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")
    # Первый ингредиент в списке (булка)
    INGREDIENT = (By.XPATH, "(//a[contains(@href, '/ingredient')])[1]")
    # Счётчик ингредиента (родительский элемент для конкретного ингредиента)
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")
    # Активное модальное окно
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'modal_active')]")
    # Кнопка закрытия модального окна (крестик)
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Номер заказа в модалке после оформления
    ORDER_ID_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'modal__title')]")
    # Кнопка "Войти в аккаунт" на главной (если пользователь неавторизован)
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Восстановить пароль"
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class RecoveryPageLocators:
    # Поле ввода email на странице восстановления
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    # Кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Иконка "показать/скрыть пароль" (глазик)
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    # Поле ввода нового пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
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
    # Первый заказ в ленте
    ORDER_ITEM = (By.XPATH, "(//li[contains(@class, 'OrderHistory_orderItem')])[1]")
    # Модалка с деталями заказа
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'modal_active')]")
    # Номера заказов в ленте
    ORDER_NUMBERS = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    # Счётчик "Выполнено за всё время"
    COMPLETED_ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # Счётчик "Выполнено за сегодня"
    COMPLETED_TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Список заказов в работе
    ORDERS_IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")