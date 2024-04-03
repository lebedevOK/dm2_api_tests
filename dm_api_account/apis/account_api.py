import requests
from requests import Response
from ..models.registration_model import RegistrationModel
from ..models.reset_password import ResetRegisteredUserPassword
from ..models.change_password import ChangeRegisteredUserPassword
from ..models.change_email import ChangeRegisteredUserEmail
from requests import session
from restclient.restclient import RestClient
from dm_api_account.models.user_envelope_model import UserEnvelopeModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """"
        :param json RegistrationModel
        Register new user
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs):
        """"
        Get current user
        :return:
        """

        response = self.client.get(
            path="/v1/account",
            **kwargs
        )
        return response

    def put_v1_account_token(self, token, **kwargs):
        """"
        Activate registered user
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        #не используем UserEnvelopeModel т.к. ожидается только токен
        #UserEnvelopeModel(**response.json())
        return response

    def post_v1_account_password(self, json: ResetRegisteredUserPassword, **kwargs) -> Response:
        """"
        :param json ResetRegisteredUserPassword
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path="/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: ChangeRegisteredUserPassword, **kwargs) -> Response:
        """"
        :param json ChangeRegisteredUserPassword
        Change registered user password
        :return:
        """

        response = self.client.put(
            path="/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self, json: ChangeRegisteredUserEmail, **kwargs) -> Response:
        """"
        :param json ChangeRegisteredUserEmail
        Change registered user email
        :return:
        """

        response = self.client.put(
            path="/v1/account/email",
            json=json,
            **kwargs
        )
        return response
