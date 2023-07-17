import requests
import time

endpoint = "http://188.40.187.241:9000/aliens"

# Start the timer
start_time = time.time()

# Make a GET request to the endpoint
response = requests.get(endpoint)

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Check the response status code to ensure successful retrieval
if response.status_code == 200:
    # Data retrieval successful
    data = response.json()  # Assuming the response contains JSON data
    # Process the data or perform any desired operations

    print("Data retrieval successful!")
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))
else:
    # Data retrieval failed
    print("Data retrieval failed. Status code:", response.status_code)

