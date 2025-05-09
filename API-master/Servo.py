import time
import pigpio

servo = 16

global ang
ang = 1500
global dc
dc = 1500

pi = pigpio.pi()
pi.set_mode(servo,pigpio.OUTPUT)
pi.set_PWM_frequency(servo,50)
pi.set_PWM_range(servo, 20000)

def look_right():
    global ang
    global dc
    if (dc == 2500 or dc > 2500):
        dc = 2500
    elif (dc <= 2500 and dc >= 500 ):
        ang = dc
        pi.set_servo_pulsewidth(servo,ang)
        dc = ang + 100

def look_left():
    global ang
    global dc
    if (dc == 500 or dc < 500):
        dc = 500
    elif (dc >= 500 and dc <= 2500):
        ang = dc
        pi.set_servo_pulsewidth(servo,ang)
        dc = ang - 100

def look_neutral():
    pi.set_servo_pulsewidth(servo,1500)
    time.sleep(0.5)

"""
def main():
    while True:
        cmd = input("-->")
        if cmd == "left":
            look_left()
        elif cmd == "right":
            look_right()
        elif cmd == "neutral":
            look_neutral()
        elif cmd == "clean":
            pi.set_servo_pulsewidth(servo,0)
            pi.stop()
        else :
            print("Not a valid command")
    return

main()"""