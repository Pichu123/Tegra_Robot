import time
import serial
import threading
import math
from inputs import *
ser = serial.Serial('/dev/ttyACM0', 115200)
left = 0
right = 0
left_bonus = 0
right_bonus = 0

def thread():
    global left, right, left_bonus, right_bonus
    while True:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            if event.ev_type == 'Absolute' and event.code=='ABS_Y':
                right = 50 * (event.state) / 32800.0
                right /= 50.0
                sign = right / abs(right)
                right *= right
                right *= 50 * sign
            if event.ev_type == 'Absolute' and event.code=='ABS_RY':
                left = 50 * (event.state) / 32800.0
                left /= 50.0
                sign = left / abs(left)
                left*=left
                left *= 50 * sign
            if event.ev_type == 'Absolute' and event.code=='ABS_Z':
                right_bonus = event.state / 255.0
            if event.ev_type == 'Absolute' and event.code=='ABS_RZ':
                left_bonus = event.state / 255.0
        time.sleep(0.001)


t = threading.Thread(target=thread)
t.daemon = True
t.start()

while True:
    lleft = -int(right + (right / 60.0) * (right_bonus + left_bonus) * 30 / 2)
    lright = -int(left + (left / 70.0) * (right_bonus + left_bonus) * 30 / 2)
    print(lleft, lright, left_bonus + right_bonus)
    ser.write([lright + 127])
    ser.write([lleft + 127])
    time.sleep(0.01)
