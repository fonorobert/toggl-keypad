from TogglPy import Toggl
import configparser, os 

configParser = configparser.RawConfigParser()


configFilePath = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/config.cfg'
configParser.read(configFilePath)

api_token = configParser.get('auth', 'api_token')

toggl = Toggl()

# this is a test accounts key. yeah, i know, api key in git is bad, whatevs
toggl.setAPIKey(api_token)

currententry = toggl.currentRunningTimeEntry()

print(currententry)
