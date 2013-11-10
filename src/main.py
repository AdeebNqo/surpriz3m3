#
# Testing
#
from notifications import notification
from device import device
from actions import actions
import lightblue

def yes():
	print('yes!')

#
# Testing notifications
#

#responses = actions(True)
#responses.funclist['yes'] = yes
#responses.funclist['no'] = yes
#notif = notification("Zola")
#notif.notify("This is a notification", notification.info, responses)

#
# Testing device connections
#
print(lightblue.finddevices())
