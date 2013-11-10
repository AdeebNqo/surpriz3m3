import lightblue
class device:
	#
	# Creating data transfer object address has to be provided
	#
	def __init__(self, address):
		self.service_ports = {}
		self.address = address
		self.ports_discovered = false
	#
	# Method for getting device services and their ports
	#
	def get_services(self):
		services = lightblue.findservices(self.address)
		return services
	#
	# Method for determining/finding service ports
	#
	def discover_service_ports(self):
		for service in self.get_services():
			self.service_ports[service[2]] = service[1]
	#
	# Method for retrieving service ports
	# @returns dictionary with port numbers, service name is the key
	def get_service_ports(self):
		if (!ports_discovered):
			self.discover_service_ports()
		return service_ports
