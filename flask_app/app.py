from flask import Flask
import pickle
import requests
import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify('Hello World!')

@app.route('/dashboard')
def dashboard():
    return jsonify(requests.post(url='http://127.0.0.1:3000/dashboard/2-stock-visualization'))

@app.route('/model')
def model():
    model = None
    with open('../model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)
    return jsonify(model)
