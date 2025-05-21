import allure
from page_objects.base_page import BasePage
from locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):

    @allure.step("Переход в личный кабинет")
    def go_to_profile(self):
        self.click(ProfileLocators.PROFILE_BUTTON)

    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        self.click(ProfileLocators.ORDER_HISTORY)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)
