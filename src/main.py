#
# Testing
#
import notif
import bluetooth
from bluzi import device
n = notif.notif("/dev/nokia", "Nokia phone")
n.notify()
try:
	d = bluetooth.discover_devices()
	trans = device(d[0])
	trans.get_services()
	#trans.send("/home/adeeb/Documents/programming/surpriz3m3/src/setup.py")
except bluetooth.btcommon.BluetoothError as this:
	print("Could not connect %s " %this)
