

import requests

endpoint = "http://127.0.0.1:8000/api/products/ultimate/"

headers = {
    "Authorization" : f"bearer fdedd3e78c25f4d7cede0225eb6127202afa040a"
}

response = requests.get(endpoint, headers=headers)

print(response.json())

