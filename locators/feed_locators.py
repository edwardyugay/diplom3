from selenium.webdriver.common.by import By

class FeedLocators:
    FEED_TAB           = (By.XPATH, "//p[text()='Лента заказов']")
    FIRST_ORDER        = (By.XPATH, "//li[contains(@class,'OrderList_item')]")
    TOTAL_ORDERS       = (By.XPATH, "//p[text()='Выполнено за все время']/following-sibling::p")
    TODAY_ORDERS       = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    ORDER_MODAL        = (By.CLASS_NAME, "OrderDetails")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_close__icon")
