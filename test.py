from TogglPy import Toggl

toggl = Toggl()

# this is a test accounts key. yeah, i know, api key in git is bad, whatevs
toggl.setAPIKey('65abbfe0c5a28d7c4e94882c7c081986')

currententry = toggl.currentRunningTimeEntry()

print(currententry)
