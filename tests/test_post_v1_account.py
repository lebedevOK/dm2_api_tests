
import time
import requests
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
import allure
from data_for_tests.create_user import new_user
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
   processors=[
       structlog.processors.JSONRenderer(indent=2, sort_keys=True, ensure_ascii=False)
   ]
)

# structlog.configure(
#     processors=[
#         structlog.processors.KeyValueRenderer()
#     ]
# )

@allure.feature('account')
@allure.story('create new account')
def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    login_gen, email_gen, password_gen = new_user()
    json_data = RegistrationModel(
        login=login_gen,
        email=email_gen,
        password=password_gen
    )
    # check_input_json(json_data)

    response = api.account.post_v1_account(json=json_data)
    #print(response)
    assert response.status_code == 201, f"Wrong status code {response.status_code}, expected 201"


    # тест на проверку токена
    # time.sleep(2)
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)
    # assert response.status_code == 200, f"Wrong status code {response.status_code}, expected 200"


# пример ручной валидации json
# def check_input_json(json_data):
#     """
#     Function to check the input JSON for the correct types of 'login', 'email', and 'password' keys.
#     """
#     for key, value in json_data.items():
#         if key == 'login':
#             assert isinstance(value, str), f"Wrong type key in {key}, expected str, got actual result {type(value)}"
#         elif key == 'email':
#             assert isinstance(value, str), f"Wrong type key in {key}, expected str, got actual result {type(value)}"
#         elif key == 'password':
#             assert isinstance(value, str), f"Wrong type key in {key}, expected str, got actual result {type(value)}"