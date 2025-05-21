import allure
from page_objects.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):

    @allure.step("Переход в конструктор")
    def go_to_constructor(self):
        self.click(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в ленту заказов")
    def go_to_feed(self):
        self.click(MainLocators.FEED_BUTTON)

    @allure.step("Открытие модального окна ингредиента")
    def open_ingredient_modal(self):
        self.click(MainLocators.INGREDIENT_ITEM)

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click(MainLocators.MODAL_CLOSE_BUTTON)
