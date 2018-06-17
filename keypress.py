# detect keypresses so we can later trigger Toggl events with them
import evdev, configparser, os
from evdev import InputDevice, categorize, ecodes

## get config

configParser = configparser.RawConfigParser()


configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/config.cfg'
configParser.read(configFilePath)

input_device = configParser.get('device', 'input_device')

## get list of all devices
#devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
#
#for device in devices:
#    print(device.path, device.name, device.phys)

# listen for events
device = InputDevice(input_device) # my keyboard
# evaluate events
for event in device.read_loop():
    # respond if S key is released
    if event.type == ecodes.EV_KEY and event.code == 31 and event.value == 00:
        print("S pressed, stop timer")
