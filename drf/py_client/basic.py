# Trying the api with the raw python client and requests
import requests

endpoint = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(endpoint)

print(response.text) # Raw jeson response will be seen on the console

