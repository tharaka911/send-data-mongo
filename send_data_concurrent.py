import requests
import json
import threading
import time

endpoint = "http://localhost:9000/aliens"

def send_data(i):
    data = {
        "name": f"no{i}_lakshan"+"k"*i,
        "tech": f"tech{i}"+"k"*i,
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
start_time = time.time()  # Start time
for i in range(1, 11):
    thread = threading.Thread(target=send_data, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()  # End time
total_time = end_time - start_time

print(f"All requests completed. Total time: {total_time} seconds.")
