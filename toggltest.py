from TogglPy import Toggl
import configparser, os 

configParser = configparser.RawConfigParser()
configFilePath = os.path.expanduser("~") + "/.togglkeypadrc"
configParser.read(configFilePath)

api_key = configParser.get('auth', 'api_token')

toggl = Toggl()

# this is a test accounts key. yeah, i know, api key in git is bad, whatevs
toggl.setAPIKey(api_key)

currententry = toggl.currentRunningTimeEntry()

print(currententry)
