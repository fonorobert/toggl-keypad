import TogglPy

toggl = TogglPy.Toggl()

toggl.setAPIKey('65abbfe0c5a28d7c4e94882c7c081986')

currententry = toggl.currentRunningTimeEntry()

print(currententry)
