from page_objects.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    def go_to_constructor(self):
        self.click(MainLocators.CONSTRUCTOR_TAB)

    def go_to_feed(self):
        self.click(MainLocators.FEED_TAB)

    def open_ingredient_modal(self):
        self.click(MainLocators.INGREDIENT_ITEM)

    def close_ingredient_modal(self):
        self.click(MainLocators.MODAL_CLOSE_BUTTON)

    def get_ingredient_counter(self):
        return self.driver.find_element(*MainLocators.INGREDIENT_COUNTER).text
