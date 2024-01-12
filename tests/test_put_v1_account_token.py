import requests
import json
from services.dm_api_account import DmApiAccount

def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')



    response = api.account.put_v1_account_token(token = '0cebc451-86a5-4677-a733-8b42ebbe3187')
    print(response)
    print(response.url)

