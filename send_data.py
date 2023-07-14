import requests
import json

endpoint = "http://localhost:9000/aliens"

for i in range(1, 1001):
    data = {
        "name": f"no{i}_lakshan",
        "tech": f"tech{i}",
        "sub": True
    }

    response = requests.post(endpoint, json=data)

    if response.status_code == 200:
        print(f"Data {i} sent successfully.")
    else:
        print(f"Failed to send data {i}. Error: {response.text}")