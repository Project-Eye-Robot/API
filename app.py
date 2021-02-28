from flask import Flask, request, jsonify
from gpiozero import LED
from time import sleep
from MotorModule import Motor
from picamera import PiCamera

app = Flask(__name__)

led = LED(17)
motor = Motor(2,3,4,17,22,27)
camera = PiCamera()


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

@app.route('/motor2', methods=['GET'])
def motor2():
    motor.move(0.6,0,2)
    motor.stop(2)

@app.route('/cameraShow', methods=['GET'])
def cameraShow():
    camera.start_preview()
    sleep(5)
    camera.stop_preview()

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
