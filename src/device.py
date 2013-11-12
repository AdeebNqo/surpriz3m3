from bluetooth import *
from OBEXClient import OBEXClient
class device:
	def __init__(self, address, port):
		self.address = address
		self.port = port
		self.client = OBEXClient(address, port)
		self.client.connect()
	def send_file(pfile):
		print("snedin file")
	def disconnect():
		self.client.disconnect()
		
