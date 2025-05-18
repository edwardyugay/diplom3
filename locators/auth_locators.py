from selenium.webdriver.common.by import By

class AuthLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESET_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    RESTORE_EMAIL_INPUT = (By.NAME, "email")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[contains(@class, 'input__icon')]")
