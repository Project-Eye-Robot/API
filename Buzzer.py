import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 100)
p.start(0)

def BuzzOn():
    p.ChangeDutyCycle(50)

def BuzzOff():
    p.ChangeDutyCycle(0)
"""
def main():
    while True:
        cmd = input("-->")

        if cmd == "buzz on":
            BuzzOn()
        elif cmd == "buzz off":
            BuzzOff()
        else:
            print("Not a valid command")
    return

main()"""