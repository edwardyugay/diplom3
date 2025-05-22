from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    EMAIL_INPUT        = (By.NAME, "email")
    RESET_BUTTON       = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD      = (By.CLASS_NAME, "input__icon")
    RESET_SUCCESS_MSG  = (By.XPATH, "//h2[contains(text(),'Восстановление отправлено')]")
