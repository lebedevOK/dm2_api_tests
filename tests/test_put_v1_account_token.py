import requests
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi()  # Создание экземпляра класса MailhogApi
    token=mailhog_api.get_token_from_last_email()

    response = api.account.put_v1_account_token(token=token)
    print(response)
    print(response.url)

