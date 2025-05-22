import allure
from page_objects.main_page import MainPage
from utils.urls import MAIN_PAGE_URL
from locators.main_locators import MainLocators

@allure.suite("Основной функционал")
class TestMainPage:

    @allure.title("Переход по кнопке 'Конструктор'")
    def test_constructor_button(self, browser):
        page = MainPage(browser)
        page.open(MAIN_PAGE_URL)
        page.go_to_constructor()
        assert page.is_displayed(MainLocators.CONSTRUCTOR_TAB)

    @allure.title("Переход по кнопке 'Лента заказов'")
    def test_feed_button(self, browser):
        page = MainPage(browser)
        page.open(MAIN_PAGE_URL)
        page.go_to_feed()
        assert page.is_displayed(MainLocators.FEED_TAB)
