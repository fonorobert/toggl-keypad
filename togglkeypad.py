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
timers = dict(configParser.items('timers'))
print(type(timers))
print(timers)


print(type(timers['1']))
print(timers['1'])
print(timers['1'][0])
timer1str = '{"projectid": 124015468, "description": "this is a TE"}'
timer1 = dict(timer1str)
print(type(timer1))
print(timer1)

exit()
# turn timers into dicts
config['timers'] = {}

for key in timers:
    print(timers[key])
    config['timers'][key] = {}
    timer_temp = dict(timers[key])
    for attr in timer_temp:
        config['timers'][key][attr] = timer_temp[attr]
    print(config['timers'][key])
    del timer_temp


print(config['timers'])
exit()

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
    toggl.startTimeEntry("started from keypad", config['projects'][projectkey])
    # get project id, start timer on project
    print("timer started on project with id " + config['projects'][projectkey])


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



