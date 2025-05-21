import allure
from page_objects.profile_page import ProfilePage
from locators.profile_locators import ProfileLocators
from utils.urls import LOGIN_PAGE_URL

@allure.suite("Личный кабинет")
class TestProfileSection:

    @allure.title("Переход в личный кабинет и выход")
    def test_profile_flow(self, browser, test_user):
        user_data, _ = test_user
        page = ProfilePage(browser)
        page.open(LOGIN_PAGE_URL)
        page.input_text(ProfileLocators.EMAIL_INPUT, user_data["email"])
        page.input_text(ProfileLocators.PASSWORD_INPUT, user_data["password"])
        page.click(ProfileLocators.LOGIN_BUTTON)
        page.go_to_profile()
        page.go_to_order_history()
        page.logout()
        assert page.is_displayed(ProfileLocators.LOGIN_BUTTON)
