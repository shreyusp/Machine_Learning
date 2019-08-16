import cv2
import numpy as np
from flask import Flask,render_template
from Adafruit_IO import Client

aio=Client('shrpoojary','21116a9cbc0e48848c4e5f0ee95d1b81')
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/left')
def left():
    #content to aio
    aio.send_data('cartrial',4)
    #capture image and save it in dir
    resp=io.imread("http://192.168.43.1:8080/shot.jpg")
    img=cv2.cvtColor(resp,cv.COOR_RGB2BGR)
    cv2.imwrite('left/image.jpg',img)
    return render_template('index.html')
@app.route('/right')
def left():
    #content to aio
    aio.send_data('cartrial',)
    #capture image and save it in dir
    resp=io.imread("http://192.168.43.1:8080/shot.jpg")
    img=cv2.cvtColor(resp,cv.COOR_RGB2BGR)
    cv2.imwrite('right/image.jpg',img)
    return render_template('index.html')
@app.route('/forward')
def left():
    #content to aio
    aio.send_data('cartrial',1)
    #capture image and save it in dir
    resp=io.imread("http://192.168.43.1:8080/shot.jpg")
    img=cv2.cvtColor(resp,cv.COOR_RGB2BGR)
    cv2.imwrite('forward/image.jpg',img)
    return render_template('index.html')
@app.route('/backward')
def left():
    #content to aio
    aio.send_data('cartrial',1)
    #capture image and save it in dir
    resp=io.imread("http://192.168.43.1:8080/shot.jpg")
    img=cv2.cvtColor(resp,cv.COOR_RGB2BGR)
    cv2.imwrite('backward/image.jpg',img)
    return render_template('index.html')

if__name__=='__main__":
    app.run(debug=True)
    