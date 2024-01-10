import requests

def put_v1_account_token():
    """"
    Activate registered user
    :return:
    """
    token = "ec7ff754-1883-4d7b-95f4-54da07db2ed7"
    url = f"http://5.63.153.31:5051/v1/account/{token}"

    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers
    )

