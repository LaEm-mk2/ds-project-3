from flask import Flask
import pickle
import requests

app = Flask(__name__)

@app.route('/')
def index():
    model = None
    with open('model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)
    return model

@app.route('/dashboard')
def dashboard():
    return requests.post(url='http://127.0.0.1:3000/dashboard/2-stock-visualization')

