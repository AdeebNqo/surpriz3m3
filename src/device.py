import bluetooth
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
		services = bluetooth.find_service(address=self.address)
		return services
	#
	# Method for retrieving all supported ports
	# -keeps p
	def get_supported_ports(self):
		services = self.get_services()
		for service in services:
			self.ports[service['name']] = service['port']
		return self.ports
	#
	# Method for checking if file transfer is supported by device
	#
	def is_filetransfer_supported(self):
		services = self.get_services();
		for service in services:
			if (service['name']=="OBEX File Transfer"):
				return True
		return False
	#
	# Method for getting port for file transfer port
	#
	def get_filetransfer_port(self):
		return ports['OBEX File Transfer']
	#
	# Method for connecting to device for particular
	# service hence the port of the service is needed
	#
	def connect(self, port):
		self.socket.connect((self.address, port))
	#
	# Method for sending data to
	# default address
	#
	def send(self, filepath):
		f = open(filepath)
		send(f)
		print("sending...")
	#
	# Method for sending data. This
	# changes address
	#
	def send(self, filepath, address):
		self.address = address

