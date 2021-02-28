import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA,GPIO.OUT)
        GPIO.setup(self.In1A,GPIO.OUT)
        GPIO.setup(self.In2A,GPIO.OUT)
        GPIO.setup(self.EnaB,GPIO.OUT)
        GPIO.setup(self.In1B,GPIO.OUT)
        GPIO.setup(self.In2B,GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA,100); # Frequency to 100
        self.pwmA.start(0); # setting duty cycle to 0
        self.pwmB = GPIO.PWM(self.EnaB,100);
        self.pwmB.start(0); # setting duty cycle to 0

    def move(self,speed=0.5,turn=0,t=0): # x is the speed , and t is the moveF time
        speed *=100
        turn *=100
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        if leftSpeed>100: leftSpeed = 100
        elif leftSpeed<-100: leftSpeed = -100
        if rightSpeed>100: rightSpeed = 100
        elif rightSpeed<-100: rightSpeed = -100

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed>0:
            GPIO.output(self.In1A,GPIO.HIGH)
            GPIO.output(self.In2A,GPIO.LOW)
        else:
            GPIO.output(self.In1A,GPIO.LOW)
            GPIO.output(self.In2A,GPIO.HIGH)

        if rightSpeed>0:
            GPIO.output(self.In1A,GPIO.HIGH)
            GPIO.output(self.In2A,GPIO.LOW)
        else:
            GPIO.output(self.In1A,GPIO.LOW)
            GPIO.output(self.In2A,GPIO.HIGH)

        sleep(t)
    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        sleep(t)



    '''
    for x in range(20,100):
        motor1.moveF(x,0.05)
        print(x)
    for x in range(100,20,-1):
        motor1.moveF(x,0.05)
        print(x)
    motor1.stop(5)
    '''