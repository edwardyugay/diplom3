from page_objects.feed_page import FeedPage

def test_order_feed_flow(browser):
    feed = FeedPage(browser)
    feed.open_first_order()
    total = int(feed.get_total_orders_count())
    today = int(feed.get_today_orders_count())
    assert total >= 0
    assert today >= 0
