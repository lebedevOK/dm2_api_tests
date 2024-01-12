import requests
import json
from services.dm_api_account import DmApiAccount

def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "login1201",
        "email": "login1201@qw.ru",
        "password": "login120100"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)
