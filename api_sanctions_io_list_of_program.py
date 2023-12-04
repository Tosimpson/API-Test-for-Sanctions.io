import requests

# API key
api_key = 'API KEY'

# API endpoint
url = "https://api.sanctions.io/programs/"

headers = {
    'Accept': 'application/json; version=2.2',
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    file_name = 'LIST OF PROGRAMS.json'  # Specify the desired file name
    
    # Save the response content to the file
    with open(file_name, 'w') as file:  # Open in text write mode, not binary
        file.write(response.text)
    
    print(f"Response saved as '{file_name}'")
else:
    print(f"Request failed with status code {response.status_code}")
