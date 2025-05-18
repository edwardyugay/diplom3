from page_objects.login_page import LoginPage
from page_objects.reset_password_page import ResetPasswordPage

def test_password_reset_flow(browser):
    login_page = LoginPage(browser)
    login_page.click_reset_password()

    reset_page = ResetPasswordPage(browser)
    reset_page.enter_email("test@example.com")
    reset_page.click_restore_button()
    assert reset_page.is_password_input_active()
    reset_page.click_show_password()
    assert reset_page.is_password_input_active()
