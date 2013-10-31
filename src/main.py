#
# Testing
#
import notif
import bluetooth
from bluzi import transfer
n = notif.notif("/dev/nokia", "Nokia phone")
n.notify()
try:
	d = bluetooth.discover_devices()
	trans = transfer(d[0])
	trans.send("/home/adeeb/Documents/programming/surpriz3m3/src")
except bluetooth.btcommon.BluetoothError:
	print("Could not connect")
