import requests
from requests import Response
from ..models.authenticate_model import AuthenticateViaCredentials
from requests import session


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers = headers

    def post_v1_account_login(self, json: AuthenticateViaCredentials, **kwargs) -> Response:
        """"
        :param json AuthenticateViaCredentials
        Authenticate via credentials
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
        return response

    def del_v1_account_login(self, **kwargs):
        """"
        Logout as current user
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )
        return response

    def del_v1_account_login_all(self, **kwargs):
        """"
        Logout from every device
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )
        return response
