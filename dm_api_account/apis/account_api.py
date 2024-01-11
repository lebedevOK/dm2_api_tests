import requests
from requests import Response
from ..models.registration_model import RegistrationModel
from ..models.reset_password import ResetRegisteredUserPassword
from ..models.change_password import ChangeRegisteredUserPassword
from ..models.change_email import ChangeRegisteredUserEmail
from requests import session


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers = headers

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """"
        :param json RegistrationModel
        Register new user
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json
                 ** kwargs
        )
        return response

    def get_v1_account(self, **kwargs):
        """"
        Get current user
        :return:
        """

        response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )
        return response

    def put_v1_account_token(self, **kwargs):
        """"
        Activate registered user
        :return:
        """
        token = "ec7ff754-1883-4d7b-95f4-54da07db2ed7"

        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetRegisteredUserPassword, **kwargs) -> Response:
        """"
        :param json ResetRegisteredUserPassword
        Reset registered user password
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
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

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
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

        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response
