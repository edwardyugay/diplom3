import pytest
import requests
from helpers.test_data import generate_user

@pytest.fixture
def test_user():
    user = generate_user()
    response = requests.post(
        "https://stellarburgers.nomoreparties.site/api/auth/register",
        json=user
    )
    if response.status_code != 200:
        raise Exception("Не удалось создать пользователя")
    token = response.json()["accessToken"].split()[-1]
    yield user, token
    requests.delete(
        "https://stellarburgers.nomoreparties.site/api/auth/user",
        headers={"Authorization": f"Bearer {token}"}
    )
