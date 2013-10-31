import bluetooth
class transfer:
	#
	# Creating data transfer object
	# port is always 1 and address has to be provided
	def __init__(self, address):
		self.port = 1
		self.address = address
		self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		self.socket.connect((address, self.port))
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

