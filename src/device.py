import lightblue
class device:
	#
	# Creating data transfer object address has to be provided
	#
	def __init__(self, address):
		self.ports = {}
		self.port = 1
		self.address = address
		self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	#
	# Method for getting device services and their ports
	#
	def get_services(self):
		services = lightblue.findservices(self.address)
		return services
