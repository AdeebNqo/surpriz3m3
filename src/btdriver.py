#
#
# AdeebNqo
# 12 EyeNkanga 2013
#
import bluetooth
def main():
	_get_service(bluetooth.discover_devices()[0])
#
# Returns a dictionary of devices
# <name, address> pair
#
def discover_devices():
	devices = {}
	devs = bluetooth.discover_devices()
	for device in devs:
		devices[bluetooth.lookup_name(device)] = device
	return devices
#
# Method for getting the service tuple
# (address, channel)
#
def _get_service(address):
	service_list = bluetooth.find_service()
	for service in service_list:
		print(service['host'])
if __name__=='__main__':
	main()
