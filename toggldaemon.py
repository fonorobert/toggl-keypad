import daemon, os
import togglkeypad

with daemon.DaemonContext():
    togglkeypad.toggl_run()

