import bluetooth
print("searching for devices...")
devices = bluetooth.discover_devices()
print("found 'em")
for device in devices:
	print(bluetooth.lookup_name(device))
class transfer:
	#
	# Creating data transfer object
		self.address = address
	# port is always 1 and address has to be provided
	def __init__(self, address):
		self.port = 1
		self.address = ""
	#
	# Method for sending data to
	# default address
	#
	def send(self, filepath):
		print("sending...")
	#
	# Method for sending data. This
	# changes address
	#
	def send(self, filepath, address):
		self.address = 
