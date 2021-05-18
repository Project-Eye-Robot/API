from flask import Flask, request,jsonify, render_template, Response
from gpiozero import LED
from time import *
import os
import threading
from camera import VideoCamera
from MotorModule import Motor
#from picamera import PiCamera

pi_camera = VideoCamera(flip=False)

app = Flask(__name__)

#led = LED(23)
motor = Motor(2,3,4,17,27,22)
#camera = PiCamera()
#camera.close()

@app.route('/')
def index():
    return 'Hello world'

@app.route('/testGet', methods=['GET'])
def testGet():
    return "test"

@app.route('/testPost', methods=['POST'])
def testPost():
    return request.json['test']

@app.route('/on', methods=['GET'])
def on():
    return led.on()

@app.route('/off', methods=['GET'])
def off():
    return led.off()

@app.route('/F',methods=['GET'])
def Forward():
    motor.move(0.4,0,0.1)
    motor.stop(2)

@app.route('/B',methods=['GET'])
def Backward():
    motor.move(-0.4,0,0.1)
    motor.stop(2)

@app.route('/R',methods=['GET'])
def Right():
    motor.move(0.4,-0.4,0.1)
    motor.stop(2)

@app.route('/L',methods=['GET'])
def Left():
    motor.move(0.4,0.4,0.1)
    motor.stop(2)


@app.route('/camera')
def stream():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')