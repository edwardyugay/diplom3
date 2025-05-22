import allure
from page_objects.feed_page import FeedPage
from utils.urls import MAIN_PAGE_URL

@allure.suite("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие и закрытие модального окна заказа")
    def test_order_detail_modal(self, browser):
        page = FeedPage(browser)
        page.open(MAIN_PAGE_URL)
        page.go_to_feed()
        page.open_first_order()
        assert page.is_order_modal_displayed()
        page.close_order_modal()
        assert not page.is_order_modal_displayed()

    @allure.title("Валидация счётчиков заказов")
    def test_order_counters_are_integers(self, browser):
        page = FeedPage(browser)
        page.open(MAIN_PAGE_URL)
        page.go_to_feed()
        total = page.get_total_orders_count()
        today = page.get_today_orders_count()
        assert isinstance(total, int)
        assert isinstance(today, int)
