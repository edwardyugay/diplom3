from selenium.webdriver.common.by import By

class ProfileLocators:
    PROFILE_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    ORDER_HISTORY = (By.LINK_TEXT, "История заказов")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
