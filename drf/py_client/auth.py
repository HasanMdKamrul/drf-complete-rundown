# Trying the api with the raw python client and requests
import getpass

import requests

# get pass

username = input("Enter username: ")
password = getpass.getpass("Enter password:")

# endpoint = "https://jsonplaceholder.typicode.com/posts/1"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/auth/"
response = requests.post(endpoint,json={"username":"admin","password": password})
print(response.json())
if response.status_code == 200:
    token = response.json()['token']
    headers = {
        "Authorization" : f"bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/ultimate/5"
    product_response = requests.get(endpoint, headers=headers)
    product_response = product_response.json()
    print(product_response)

# print(response.text)
 # Raw jeson response will be seen on the console

# print(response.status_code)
