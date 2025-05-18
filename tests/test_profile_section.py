from page_objects.profile_page import ProfilePage

def test_profile_flow(browser, test_user):
    user_data, token = test_user

    browser.get("https://stellarburgers.nomoreparties.site/login")
    from selenium.webdriver.common.by import By
    browser.find_element(By.NAME, "name").send_keys(user_data["email"])
    browser.find_element(By.NAME, "Пароль").send_keys(user_data["password"])
    browser.find_element(By.XPATH, "//button[text()='Войти']").click()

    profile = ProfilePage(browser)
    profile.go_to_profile()
    profile.go_to_order_history()
    profile.logout()
