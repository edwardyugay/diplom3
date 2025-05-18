from selenium.webdriver.common.by import By

class FeedLocators:
    FIRST_ORDER = (By.XPATH, "//li[contains(@class,'OrderList_item')]")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
