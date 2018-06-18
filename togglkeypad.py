from TogglPy import TogglPy
import configparser, os, evdev, sys 

# load config
configParser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/config.cfg'
configParser.read(configFilePath)

config = {}
config['api_token'] = configParser.get('auth', 'api_token')
config['device_path'] = configParser.get('device', 'input_device')
config['keys'] = dict(configParser.items('keys'))
config['projects'] = dict(configParser.items('projects'))



def stop():
    # stop timer
    print("timer stopped")

def start(project):
    # get project id, start timer on project
    print("timer started on project " + project)


def key_react(key_pressed):
    keys = config['keys']
    projects = config['projects']

    if key != '0':
        start(key)
    else:
        stop()




# set up key event listener
device = evdev.InputDevice(config['device_path'])
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.value == 00:
        #only release key events here

        #switch statement comes here


        for key in config['keys']:
            
            if int(config['keys'][key]) == event.code:
                key_react(key)


#toggl = TogglPy.Toggl()

#toggl.setAPIKey(config['api_token'])

#currententry = toggl.currentRunningTimeEntry()

#print(currententry)
