#!/usr/bin/python
import sys
import pynotify
 
if __name__ == "__main__":
    if not pynotify.init("icon-summary-body"):
        sys.exit(1)
 
    n = pynotify.Notification(
        "Burhan Uddin",
        "What is life? Full of of care? We have no time to stand or stare!",
        "notification-message-im")
    n.show()
