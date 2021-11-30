import json

import requests

response = requests.get("https://randomuser.me/api")
print("Randomuser response code is: ", response)
print("Randomuser response body is: ", response.text)
print()

response1 = requests.get("https://api.thedogapi.com/v1/breeds")
print("Thedogapi response code is: ", response1)
print("Thedogapi response body is: ", response1.text)
print("Thedogapi response body by JSON is: ", json.dumps(response1.json(), indent=2))
print("Thedogapi response headers is: ", response1.headers)
print("Thedogapi response headers content-type is: ", response1.headers.get('content-type'))
print("Thedogapi response status_code is: ", response1.status_code)
print("Thedogapi response reason is: ", response1.reason)
request = response1.request
print("Thedogapi request type is: ", request)
print("Thedogapi request URL is: ", request.url)
print("Thedogapi request path URL is: ", request.path_url)
print("Thedogapi request method is: ", request.method)
print("Thedogapi request headers is: ", request.headers)
print()

headers = {'x-dns-prefetch-control': 'off', 'x-frame-options': 'SAMEORIGIN'}
response2 = requests.get("https://api.thedogapi.com/v1/breeds", headers=headers)
print("Thedogapi request headers for added headers is: ", response2.request.headers)
