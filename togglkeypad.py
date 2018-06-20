from TogglPy import TogglPy
import configparser, os, evdev, sys, json

class TogglKeypad(object):
    def __init__(self):
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

        self.config = config
        self.toggl = toggl


    def stop(self):
        config = self.config
        toggl = self.toggl
        # stop timer
        currententry = toggl.currentRunningTimeEntry()
        if currententry['data'] is None:
            print("no timer running")
        else:
            toggl.stopTimeEntry(currententry['data']['id'])
            print("timer stopped")

    def start(self, projectkey):
        
        config = self.config
        toggl = self.toggl
        # set up local copies

        timer = config['timers'][projectkey]
        project = timer['projectid'] if 'projectid' in timer else None 
        description = timer['description'] if 'description' in timer else None 
        task = timer['taskid'] if 'taskid' in timer else None 

        # clear project if task is present to make sure there is no conflict
        project = None if task else project

        toggl.startTimeEntry(description if description else "", project if project else None, task if task else None)


    def key_react(self, key_pressed):
        config = self.config
        toggl = self.toggl
        keys = config['keys']

        if key != 'stop':
            self.start(key)
        else:
            self.stop()


    def run(self):

        config = self.config
        toggl = self.toggl

        # set up key event listener
        device = evdev.InputDevice(config['device_path'])
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY and event.value == 00:
                #only release key events here

                #switch statement comes here


                for key in config['keys']: 
                    if int(config['keys'][key]) == event.code:
                        self.key_react(key)



