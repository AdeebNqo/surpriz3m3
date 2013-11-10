#
# Testing
#
from notifications import notification
from device import device
from actions import actions
import lightblue
import time

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

selected_device = None
found_devices=[]
for i in range(2):
	print("searching for bt device...")
	found_devices = lightblue.finddevices()
	if (len(found_devices) > 0):
		selected_device = lightblue.selectdevice()
		break
	print('No devices found')
	if (i!=2):
		print("will retry in 20 seconds.")
		time.sleep(20)

if (selected_device==None):
	print('Issues with blutooth? Eish...suckz bein\' u.')
