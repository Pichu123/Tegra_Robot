from networktables import NetworkTables
from inputs import *
NetworkTables.initialize(server='tegra-ubuntu')
#NetworkTables.initialize(server='localhost')
table = NetworkTables.getTable('RobotControl')
while True:
    events = get_gamepad()
    print(events)
    for event in events:
        print(event.ev_type, event.code, event.state)
        if event.ev_type == 'Absolute' and event.code=='ABS_Y':
            table.putNumber('leftMotor', 40 * (event.state) / 32800.0)
        if event.ev_type == 'Absolute' and event.code=='ABS_RY':
            table.putNumber('rightMotor', 50 * (event.state) / 32800.0)
