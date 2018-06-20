from TogglPy import TogglPy
import configparser, os, evdev, sys, json

# load config
configParser = configparser.RawConfigParser()
configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/config.cfg'
configParser.read(configFilePath)

config = {}
config['api_token'] = configParser.get('toggl', 'api_token')
config['ws_id'] = configParser.get('toggl', 'ws_id')
config['device_path'] = configParser.get('device', 'input_device')
config['keys'] = dict(configParser.items('keys'))
timers = dict(configParser.items('timers'))

# turn timers into dicts
config['timers'] = {}

for key in timers:
    config['timers'][key] = {}
    timer_temp = json.loads(timers[key])
    for attr in timer_temp:
        config['timers'][key][attr] = timer_temp[attr]

print(config['timers'])


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

def start(projectkey):
    
    # set up local copies

    timer = config['timers'][projectkey]
    project = timer['projectid'] if timer['projectid'] else False 
    description = timer['description'] if timer['description'] else False 
#    task = timer['task'] if timer['task'] else False 

    toggl.startTimeEntry(description if description else "", project if project else None)
    # get project id, start timer on project
#    print("timer started on project with id " + config['projects'][projectkey])


def key_react(key_pressed):
    keys = config['keys']

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



