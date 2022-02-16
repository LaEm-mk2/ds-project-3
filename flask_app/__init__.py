from flask import Flask,render_template,request
import pickle
import requests
import jsonify
import numpy as np

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def main():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def home():
    model=pickle.load(open('C:/Users/limbu/Desktop/Section3/ds-project-3/flask_app/model/model.pkl','rb'))
    date_str = str(request.form['a'])
    value = 438000000000000
    stocks = 5969782500
    per = 11.35
    per_new = 1135
    sales = 74300000000000
    gdp = 2260000000000000
    sum_price = 2680000000000000
    buffett = 118.58
    arr = np.array([[value,stocks,per,per_new,sales,gdp,sum_price,buffett]])
    pred = model.predict(arr)
    return render_template('after.html',data=pred)
    

if __name__ == '__main__':
    app.run(debug=True)