import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    else:
        raise ValueError("Браузер не поддерживается")

    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

import pytest
import requests
from faker import Faker
from utils.api_helper import delete_user

fake = Faker()

@pytest.fixture
def test_user():
    user = {
        "email": fake.email(),
        "password": "123456",
        "name": fake.first_name()
    }

    response = requests.post(
        "https://stellarburgers.nomoreparties.site/api/auth/register",
        json=user
    )
    assert response.status_code == 200, "Пользователь не создан"
    token = response.json()["accessToken"].split()[-1]

    yield user, token

    delete_user(token)
