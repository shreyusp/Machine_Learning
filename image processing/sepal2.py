from flask import Flask,request,render_template
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

from sklearn.externals import joblib
app=Flask(__name__,static_folder='public')
@app.route('/')
def index():
    return render_template('index1.html') 

@app.route('/display',methods=['POST'])
def display():
    model=joblib.load('irisPred.sav')
    sl=eval(request.form.get("sepallength"))
    sw=eval(request.form.get("sepalwidth"))
    pl=eval(request.form.get("petallength"))
    pw=eval(request.form.get("petallength"))
    pred=model.predict([[sl,sw,pl,pw]])
    flowers={0:"Setosa",1:"Versicolor",2:"Virginica"}
    return """<html><body>The flower is {}""".format(flowers[pred[0]])+"""<br>
<img src='public/"""+flowers[pred[0]].lower()+""".jpeg'></body></html>"""


if __name__=='__main__':
    app.run(debug=True)