from page_objects.base_page import BasePage
from locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):
    def go_to_profile(self):
        self.click(ProfileLocators.PROFILE_BUTTON)

    def go_to_order_history(self):
        self.click(ProfileLocators.ORDER_HISTORY)

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)
