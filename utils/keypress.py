# detect keypresses so we can later trigger Toggl events with them
import evdev, configparser, os, sys
from evdev import InputDevice, categorize, ecodes

## get command line argument



## get config
#
#configParser = configparser.RawConfigParser()
#configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/config.cfg'
#configParser.read(configFilePath)
#
#input_device = configParser.get('device', 'input_device')

def list_devices():
    # get list of all devices
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    
    for device in devices:
        print(device.path, device.name, device.phys)

def listen(input_device):
    # listen for events
    
    device = InputDevice(input_device) # my keyboard
    # evaluate events
    for event in device.read_loop():
        # respond if S key is released
        if event.type == ecodes.EV_KEY and event.code == 31 and event.value == 00:
            print(evdev.categorize(event))

if sys.argv[1]:
    if sys.argv[1] == "listen":
        listen(sys.argv[2])
    elif sys.argv[1] == "list":
        list_devices()
