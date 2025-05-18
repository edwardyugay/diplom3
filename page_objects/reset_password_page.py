from page_objects.base_page import BasePage
from locators.auth_locators import AuthLocators

class ResetPasswordPage(BasePage):
    def enter_email(self, email):
        self.input_text(AuthLocators.RESTORE_EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click(AuthLocators.RESTORE_BUTTON)

    def click_show_password(self):
        self.click(AuthLocators.SHOW_PASSWORD_BUTTON)

    def is_password_input_active(self):
        return self.is_element_present(AuthLocators.SHOW_PASSWORD_BUTTON)
