from TogglPy import TogglPy
import configparser, os, evdev, sys 

# load config
configParser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/config.cfg'
configParser.read(configFilePath)

config = {}
config['api_token'] = configParser.get('toggl', 'api_token')
config['ws_id'] = configParser.get('toggl', 'ws_id')
config['device_path'] = configParser.get('device', 'input_device')
config['keys'] = dict(configParser.items('keys'))
config['projects'] = dict(configParser.items('projects'))


# connect to Toggl
toggl = TogglPy.Toggl()

toggl.setAPIKey(config['api_token'])



#print(currententry)



def stop():
    # stop timer
    currententry = toggl.currentRunningTimeEntry()
    if currententry['data'] is None:
        print("no timer running")
    else:
        toggl.stopTimeEntry(currententry['data']['id'])
        print("timer stopped")

def start(project):
    # get project id, start timer on project
    print("timer started on project " + project)


def key_react(key_pressed):
    keys = config['keys']
    projects = config['projects']

    if key != 'stop':
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



