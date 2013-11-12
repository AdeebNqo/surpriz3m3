#
#
# AdeebNqo
# 12 EyeNkanga 2013
#
import bluetooth
from device import device

def main():
	devices = discover_devices()
	ss = supported_services(devices['Zola'])
	for service in ss:
		print(service)
	x = raw_input('Chosen service: ')
	
	st = _get_service_tuple(devices['Zola'], x)
	phone = device(st[0],st[1])
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
def _get_service_tuple(address, service_name):
	service_list = bluetooth.find_service()
	for service in service_list:
		if (service['host']==address):
			if (service['name']==service_name):
				return (address, service['port'])
	return None
#
# Method for getting all supported services by name
#
def supported_services(address):
	supported_serv = []
	service_list = bluetooth.find_service()
	for service in service_list:
		if (service['host']==address):
			supported_serv.append(service['name'])
	return supported_serv

if __name__=='__main__':
	main()
