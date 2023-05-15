#request test
import requests

# Define the endpoint URL for the API
endpoint_url = "https://jsonplaceholder.typicode.com/posts"

# Define the parameters to send with the API request
params = {
    "userId": 1,
    "id": 1
}

# Send the API request using the GET method
response = requests.get(endpoint_url, params=params)

# Check the status code of the response
if response.status_code == 200:
    # If the request was successful, print the response data
    data = response.json()
    print(data)
else:
    # If the request was unsuccessful, print the error message
    error_message = f"Error: {response.status_code} - {response.reason}"
    print(error_message)