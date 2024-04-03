import requests
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
import allure

# БЕЗ АКТИВАЦИИ АККАУНТА НЕ РАБОТАЕТ!
# def test_put_v1_account_token()
@allure.feature('login')
@allure.story('account login')
def test_post_v1_account_login():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "login1803",
        "password": "login180300",
        "rememberMe": True
    }
    response = api.login.post_v1_account_login(json=json)
    assert response.status_code == 200, f"Wrong status code {response.status_code}, expected 200"

    print(response)
    print(response.json())
    print(response.status_code)
