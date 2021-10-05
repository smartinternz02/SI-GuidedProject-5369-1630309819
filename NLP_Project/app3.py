# -*- coding: utf-8 -*-
import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model


app = Flask(__name__)

movie = load_model("movie.h5")
cv=load("transform4.save")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
   
    o = request.form['review']

    prediction=movie.predict(cv.transform([o]))
    

    if prediction > 0.5 :
        output = "Positive Movie Review"
    else:
        output="Negative Movie Review"

    return render_template('index.html', prediction_text='Result: {}'.format(output))

if __name__ == "__main__":
    app.run(port=8086,debug=True)