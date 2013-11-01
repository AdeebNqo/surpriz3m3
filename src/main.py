#
# Testing
#
from notifications import notification
import bluetooth
from device import device
from actions import actions

def yes():
	print('yes!')
try:
	#
	# Testing notifications
	#
	responses = actions(True)
	responses.funclist['yes'] = yes
	responses.funclist['no'] = yes
	notif = notification("Zola")
	notif.notify("This is a notification", notification.info, responses)
	#
	# Testing device connections
	#
	d = bluetooth.discover_devices()
	trans = device(d[0])
	print(trans.get_services())
	trans.connect(10)
	#trans.send("/home/adeeb/Documents/programming/surpriz3m3/src/setup.py")
except bluetooth.btcommon.BluetoothError as this:
	print("Could not connect %s " %this)
