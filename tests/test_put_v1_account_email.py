import requests
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
import allure

@allure.feature('email')
@allure.story('account email')
def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "login1802",
        "password": "login180200",
        "email": "string1803@qw.ru"
    }
    response = api.account.put_v1_account_email(json=json)
    assert response.status_code == 200, f"Wrong status code {response.status_code}, expected 200"

    print(response)
    print(response.json())
    print(response.status_code)
