import requests

url = "http://5.63.153.31:5051/v1/account"

payload = {}
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Accept': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)