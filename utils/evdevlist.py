# detect keypresses so we can later trigger Toggl events with them
import evdev

## get list of all devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    print(device.path, device.name, device.phys)

