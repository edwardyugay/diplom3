import allure
from page_objects.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):

    @allure.step("Ввод email для восстановления пароля")
    def enter_email(self, email):
        self.input_text(ResetPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Нажатие кнопки 'Восстановить'")
    def submit_reset(self):
        self.click(ResetPasswordLocators.RESET_BUTTON)

    @allure.step("Клик по кнопке 'Показать/Скрыть пароль'")
    def toggle_password_visibility(self):
        self.click(ResetPasswordLocators.SHOW_PASSWORD)
