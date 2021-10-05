# -*- coding: utf-8 -*-
import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model("bank.h5")
sc = load("transform3.save")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    z = request.form['job']
    if (z == "admin."):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 1,0,0,0,0,0,0,0,0,0,0,0
    if (z == "blue-collar"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,1,0,0,0,0,0,0,0,0,0,0
    if (z == "entrepreneur"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,1,0,0,0,0,0,0,0,0,0
    if (z == "housemaid"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,1,0,0,0,0,0,0,0,0
    if (z == "management"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,1,0,0,0,0,0,0,0
    if (z == "retired"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,1,0,0,0,0,0,0
    if (z == "self-employed"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,0,1,0,0,0,0,0
    if (z == "services"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,0,0,1,0,0,0,0
    if (z == "student"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,0,0,0,1,0,0,0
    if (z == "technician"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,0,0,0,0,1,0,0
    if (z == "unemployed"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,0,0,0,0,0,1,0
    if (z == "unknown"):
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12 = 0,0,0,0,0,0,0,0,0,0,0,1
    a = request.form['marital']
    if (a == "divorced"):
        a1,a2,a3 = 1,0,0
    if (a == "married"):
        a1,a2,a3 = 0,1,0
    if (a == "single"):
        a1,a2,a3 = 0,0,1
    b = request.form['education']
    if(b=="primary"):
        b1,b2,b3,b4 = 1,0,0,0
    if(b=='secondary'):
    	b1,b2,b3,b4 = 0,1,0,0
    if(b=='tertiary'):
        b1,b2,b3,b4 = 0,0,1,0
    if(b=='unknown'):
        b1,b2,b3,b4 = 0,0,0,1
    c = request.form['default']
    if(c=="no"):
        c1,c2 = 1,0
    if(c=="yes"):
        c1,c2 = 0,1
    d = request.form['housing']
    if(d=="no"):
        d1,d2 = 1,0
    if(d=="yes"):
        d1,d2 = 0,1
    e = request.form['loan']
    if(e=="no"):
        e1,e2 = 1,0
    if(e=="yes"):
        e1,e2 = 0,1
    f = request.form['contact']
    if(f=="cellular"):
        f1,f2,f3 = 1,0,0
    if(f=="telephone"):
        f1,f2,f3 = 0,1,0
    if(f=="unknown"):
        f1,f2,f3 = 0,0,1
    g = request.form['month']
    if (g == "apr"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 1,0,0,0,0,0,0,0,0,0,0,0
    if (g == "aug"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,1,0,0,0,0,0,0,0,0,0,0
    if (g == "dec"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,1,0,0,0,0,0,0,0,0,0
    if (g == "feb"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,1,0,0,0,0,0,0,0,0
    if (g == "jan"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,1,0,0,0,0,0,0,0
    if (g == "jul"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,0,1,0,0,0,0,0,0
    if (g == "jun"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,0,0,1,0,0,0,0,0
    if (g == "mar"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,0,0,0,1,0,0,0,0
    if (g == "may"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,0,0,0,0,1,0,0,0
    if (g == "nov"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,0,0,0,0,0,1,0,0
    if (g == "oct"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,0,0,0,0,0,0,0,1,0
    if (g == "sep"):
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12 = 0,0,0,1,0,0,0,0,0,0,0,1
    h = request.form['poutcome']
    if (h == "failure"):
        h1,h2,h3,h4 = 1,0,0,0
    if (h == "other"):
        h1,h2,h3,h4 = 0,1,0,0
    if (h == "success"):
        h1,h2,h3,h4 = 0,0,1,0
    if (h == "unknown"):
        h1,h2,h3,h4 = 0,0,0,1
    i = request.form['age']
    j = request.form['balance']
    k = request.form['day']
    l = request.form['duration']
    m = request.form['campaign']
    n= request.form['pdays']
    o = request.form['previous']
    total = [[o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,a1,a2,a3,b1,b2,b3,b4,c1,c2,d1,d2,e1,e2,f1,f2,f3,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12, h1,h2,h3,h4,i,j,k,l,m,n,o]]
    prediction = model.predict(sc.transform(total))
    

    if((prediction[0]==1).any()):
        output = "He|She deposited in Bank"
    else:
        output="He|She did not deposit from Bank"

    return render_template('index.html', prediction_text='Result: {}'.format(output))

if __name__ == "__main__":
    app.run(port=8086,debug=True)

