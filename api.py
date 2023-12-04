from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/api_sanctions_io_individual', methods=['GET'])
def run_sanctions_api():
    # Get parameters from the URL
    api_key = 'API KEY' 
    min_score = request.args.get('min_score')
    data_source = request.args.get('data_source')
    name = request.args.get('name')
    entity_type = request.args.get('entity_type')
    country_residence = request.args.get('country_residence')

    # Your code here (the code you provided)
    url = "https://api.sanctions.io/search/"
    query_parameters = {
        'min_score': min_score,
        'data_source': data_source,
        'name': name,
        'entity_type': entity_type,
        'country_residence': country_residence
    }
    headers = {
        'Accept': 'application/json; version=2.2',
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(url, headers=headers, params=query_parameters)

    if response.status_code == 200:
        file_name = f'response_data_{int(time.time())}.json'
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return jsonify({'message': f'Response saved as {file_name}'})
    else:
        return jsonify({'error': f'Request failed with status code {response.status_code}'})

if __name__ == '__main__':
    app.run(debug=True)



# http://127.0.0.1:5000/api_sanctions_io_individual?api_key=API KEY&min_score=0.85&data_source=SDN,HM%20Treasury&name=Alexandr%20Grigorievich%20Lukashenko&entity_type=individual&country_residence=by
# API KEY