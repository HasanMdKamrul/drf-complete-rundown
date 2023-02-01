# Trying the api with the raw python client and requests
import requests

# endpoint = "https://jsonplaceholder.typicode.com/posts/1"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
response = requests.get(endpoint)

# print(response.text)
print(response.json()["message"]) # Raw jeson response will be seen on the console

print(response.status_code)

