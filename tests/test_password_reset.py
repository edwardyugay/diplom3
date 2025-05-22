import allure
from page_objects.reset_password_page import ResetPasswordPage
from utils.urls import BASE_URL
from locators.reset_password_locators import ResetPasswordLocators

@allure.suite("Восстановление пароля")
class TestResetPassword:

    @allure.title("Ввод email и нажатие кнопки восстановления")
    def test_reset_password_email_flow(self, browser):
        page = ResetPasswordPage(browser)
        page.open(f"{BASE_URL}/forgot-password")
        page.enter_email("test@example.com")
        page.submit_reset()
        assert page.is_displayed(ResetPasswordLocators.RESET_SUCCESS_MSG)
