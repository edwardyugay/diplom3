from page_objects.main_page import MainPage

def test_main_page_navigation(browser):
    page = MainPage(browser)
    page.go_to_constructor()
    page.go_to_feed()
    page.open_ingredient_modal()
    page.close_ingredient_modal()
