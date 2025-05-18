from page_objects.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):
    def open_first_order(self):
        self.click(FeedLocators.FIRST_ORDER)

    def get_total_orders_count(self):
        return self.driver.find_element(*FeedLocators.TOTAL_ORDERS).text

    def get_today_orders_count(self):
        return self.driver.find_element(*FeedLocators.TODAY_ORDERS).text
