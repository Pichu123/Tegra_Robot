from networktables import NetworkTables
import time
NetworkTables.initialize(server=None)
table = NetworkTables.getTable('RobotControl')
import serial
ser = serial.Serial('/dev/ttyACM0', 57600)
while True:
    right = int(table.getNumber('leftMotor', defaultValue=0))
    left = int(table.getNumber('rightMotor', defaultValue=0))
    print(left, right)
    ser.write([-left + 127])
    ser.write([-right + 127])
    time.sleep(0.015)
