import allure
from page_objects.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):

    @allure.step("Переключение на вкладку «Лента заказов»")
    def go_to_feed(self):
        self.click(FeedLocators.FEED_TAB)

    @allure.step("Открытие первого заказа в списке")
    def open_first_order(self):
        self.click(FeedLocators.FIRST_ORDER)

    @allure.step("Получение количества выполненных заказов за всё время")
    def get_total_orders_count(self) -> int:
        text = self.get_text(FeedLocators.TOTAL_ORDERS)
        return int(text)

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_today_orders_count(self) -> int:
        text = self.get_text(FeedLocators.TODAY_ORDERS)
        return int(text)

    @allure.step("Проверка, что окно деталей заказа отображается")
    def is_order_modal_displayed(self) -> bool:
        return self.is_displayed(FeedLocators.ORDER_MODAL)

    @allure.step("Закрытие окна деталей заказа")
    def close_order_modal(self):
        self.click(FeedLocators.MODAL_CLOSE_BUTTON)
