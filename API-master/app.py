from flask import Flask, request,jsonify, render_template, Response
from gpiozero import LED
from time import *
import os
import threading
from camera import VideoCamera
from MotorModule import Motor
from Buzzer import *
from LED import *
from Servo import *

#from picamera import PiCamera

pi_camera = VideoCamera(flip=False)

app = Flask(__name__)

#led = LED(23)
motor = Motor(2,3,4,17,27,22)
#camera = PiCamera()
#camera.close()

@app.route('/')
def index():
    look_neutral()
    return 'Hello world'

@app.route('/testGet', methods=['GET'])
def testGet():
    return "test"

@app.route('/testPost', methods=['POST'])
def testPost():
    return request.json['test']

@app.route('/camera_right', methods=['GET'])
def camera_look_right():
    look_right()

@app.route('/camera_left', methods=['GET'])
def camera_look_left():
    look_left()

@app.route('/lightOn', methods=['GET'])
def RGB_On():
    purpleOn()

@app.route('/lightOff', methods=['GET'])
def RGB_Off():
    purpleOff()

@app.route('/honkOn', methods=['GET'])
def Buzz_On():
    BuzzOn()

@app.route('/honkOff', methods=['GET'])
def Buzz_Off():
    BuzzOff()

@app.route('/F',methods=['GET'])
def Forward():
    motor.move(0.4,0,0.1)

@app.route('/B',methods=['GET'])
def Backward():
    motor.move(-0.4,0,0.1)

@app.route('/R',methods=['GET'])
def Right():
    motor.move(0.4,-0.4,0.1)

@app.route('/L',methods=['GET'])
def Left():
    motor.move(0.4,0.4,0.1)

@app.route('/Stop',methods=['GET'])
def Stop():
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
