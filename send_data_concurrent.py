import requests
import json
import threading

endpoint = "http://localhost:9000/aliens"

def send_data(i):
    data = {
        "name": f"no{i}_lakshan"+"t"*i,
        "tech": f"tech{i}"+"t"*i,
        "sub": True
    }

    response = requests.post(endpoint, json=data)

    if response.status_code == 200:
        print(f"Data {i} sent successfully.")
    else:
        print(f"Failed to send data {i}. Error: {response.text}")

# Create a list to store the thread objects
threads = []

# Launch concurrent requests
for i in range(1, 1001):
    thread = threading.Thread(target=send_data, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All requests completed.")