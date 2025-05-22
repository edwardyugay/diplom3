from page_objects.base_page import BasePage
from locators.auth_locators import AuthLocators

class LoginPage(BasePage):
    def click_reset_password(self):
        self.click(AuthLocators.RESET_PASSWORD_LINK)
