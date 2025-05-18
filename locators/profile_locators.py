from selenium.webdriver.common.by import By

class ProfileLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
