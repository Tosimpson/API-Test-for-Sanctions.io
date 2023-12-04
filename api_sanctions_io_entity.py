import requests
import time

# API key
api_key = 'API_KEY'

# API endpoint
url = "https://api.sanctions.io/search/"

# Define the query parameters in a dictionary
query_parameters = {
    'min_score': 0.85,
    'data_source': 'SDN,HM Treasury',
    'name': 'rosbank',
    'entity_type': 'entity',
    'country_residence': 'ru'
}

payload={}
headers = {
    'Accept': 'application/json; version=2.2',
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers, params=query_parameters, data=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Generate a unique file name with a timestamp
    timestamp = int(time.time())
    file_name = f'response_data_{timestamp}.json'
    
    # Save the response content to the file
    with open(file_name, 'wb') as file:
        file.write(response.content)
    
    print(f"Response saved as '{file_name}'")
else:
    print(f"Request failed with status code {response.status_code}")
