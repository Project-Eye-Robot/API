from flask import Flask, request, jsonify
from gpiozero import LED
from time import *
import os
import subprocess
#from MotorModule import Motor
#from picamera import PiCamera
from time import sleep
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

app = Flask(__name__)

#led = LED(17)
#motor = Motor(2,3,4,17,22,27)
#camera = PiCamera()
#camera.close()

#raspivid = subprocess.Popen("raspivid -o video/" + time.strftime("%d_%b_%Y_%H_%M_%S") + " -t 36000000", shell=True)
#os.kill(raspivid.pid, signal.SIGKILL)

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

#@app.route('/motor2', methods=['GET'])
#def motor2():
    #motor.move(0.6,0,2)
    #motor.stop(2)

@app.route('/cameraShow', methods=['GET'])
def cameraShow():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    # allow the camera to warmup
    time.sleep(0.1)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')