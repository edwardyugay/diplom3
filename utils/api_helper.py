import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def delete_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(f"{BASE_URL}/auth/user", headers=headers)
