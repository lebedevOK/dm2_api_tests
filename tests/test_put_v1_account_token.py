import requests
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
import allure
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=2, sort_keys=True, ensure_ascii=False)
    ]
)
@allure.feature('token')
@allure.story('account token')
def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi()  # Создание экземпляра класса MailhogApi
    token=mailhog_api.get_token_from_last_email()

    response = api.account.put_v1_account_token(token=token)
    assert response.status_code == 200, f"Wrong status code {response.status_code}, expected 200"



