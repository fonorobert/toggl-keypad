# detect keypresses so we can later trigger Toggl events with them
import evdev
from evdev import InputDevice, categorize, ecodes

## get list of all devices
#devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
#
#for device in devices:
#    print(device.path, device.name, device.phys)

# listen for events
device = InputDevice("/dev/input/event20") # my keyboard
# evaluate events
for event in device.read_loop():
    # respond if S key is released
    if event.type == ecodes.EV_KEY and event.code == 31 and event.value == 00:
        print("S pressed, stop timer")
