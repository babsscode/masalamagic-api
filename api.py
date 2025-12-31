# api.py

from flask import Flask, jsonify, request
from foodGenerator import get_recs
from foodGenerator import get_recs2
from flask_cors import CORS
from algorithms import searchAlg, randomAlg

app = Flask(__name__)
#CORS(app, origins="*")
cors = CORS(app, resources={r"/api/*": {"origins": "https://ammaruchiai.web.app"}})

@app.route('/searchFoods', methods=['POST'])
def receive_search_data():
    data = request.get_json()
    if 'phrase' not in data:
        return jsonify({'error': 'Please provide a phrase'}), 400
    phrase = data['phrase']
    response = searchAlg(phrase)
    return response

@app.route('/randomFoods', methods=['GET'])
def receive_rand_data():
    response = randomAlg()
    return response

@app.route('/api', methods=['GET'])
def send_data():
    data = get_recs('fun and easy snacks for kids', 10)
    fixed_data = replace_nan(data)
    response = jsonify(fixed_data)
    return response

@app.route('/api', methods=['POST'])
def receive_data():
    data = request.json
    print(data, "--------------------------------")

    phrase = data.get('phrase', '')
    offset = data.get('offset')

    data = get_recs(phrase, offset)
    fixed_data = replace_nan(data)
    response = jsonify(fixed_data)
    return response

# new api
@app.route('/newapi', methods=['GET'])
def send_data2():
    data = get_recs2('fun and easy snacks for kids', 10)
    fixed_data = replace_nan(data)
    response = jsonify(fixed_data)
    return response

@app.route('/newapi', methods=['POST'])
def receive_data2():
    data = request.json 
    print(data, "--------------------------------")

    phrase = data.get('phrase', '')
    offset = data.get('offset')

    data = get_recs2(phrase, offset)
    fixed_data = replace_nan(data)
    response = jsonify(fixed_data)
    return response

def replace_nan(obj):
    if isinstance(obj, dict):
        return {key: replace_nan(val) for key, val in obj.items()}
    elif isinstance(obj, list):
        return [replace_nan(item) for item in obj]
    elif isinstance(obj, str) and obj.lower() == "nan":
        return None
    else:
        return obj

if __name__ == '__main__':
    app.run(debug=True)
