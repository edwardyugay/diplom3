from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_ITEM = (By.CLASS_NAME, "burger-ingredient")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "modal-close-icon")
    CONSTRUCTOR_TAB = (By.XPATH, "//h1[text()='Соберите бургер']")
    FEED_TAB = (By.XPATH, "//h1[text()='Лента заказов']")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")
