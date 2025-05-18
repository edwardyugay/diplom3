from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, "//p[text()='Лента заказов']")
    INGREDIENT_ITEM = (By.CLASS_NAME, "burger-ingredient")  # уточни при тестировании
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_close__")  # уточни при тестировании
