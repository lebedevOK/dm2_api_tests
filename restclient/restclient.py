from pprint import pprint

from requests import session, Response
import structlog
import uuid
import curlify


class RestClient():
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')

    def post(self, path:str, **kwargs) -> Response:
        return self._send_request('POST', path, **kwargs)

    def get(self, path:str, **kwargs) -> Response:
        return self._send_request('GET', path, **kwargs)

    def put(self, path:str, **kwargs) -> Response:
        return self._send_request('PUT', path, **kwargs)

    def _send_request(self, method, path, **kwargs):
        full_url = f"{self.host}{path}"
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            method=method,
            full_url=full_url,
            params=kwargs.get('params'),
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data'),
        )
        response = self.session.request(
            method=method,
            url=full_url,
            **kwargs
        )
        curl = curlify.to_curl(response.request)
        pprint(curl)
        log.msg(
            event='response',
            status_code=response.status_code,
            headers=response.headers,
            #json=response.json(),
            text=response.text,
            content=response.content,
            curl=curl
        )
        if 'application/json' in response.headers.get('Content-Type', ''):
            json_response = response.json()
            log.msg(event='json', json=json_response)
        return response

