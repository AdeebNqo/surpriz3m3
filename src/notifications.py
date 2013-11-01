#
# Z. Mahlaza
# Class for notifying when device  detected
#
import pynotify
class notifications:
	#
	# Notification types
	#
	info = "dialog-information"
	
	def __init__(self, devicePath, deviceName):
		self.title = "Music exchange"
		self.deviceName = deviceName
	def notify(self, msg, notif_type, actions):
		pynotify.init(self.title)
		self.notif = pynotify.Notification("Connected "+self.deviceName, msg, )
		if (actions.activated):
			self.notif.add_action("action_delete", "Yes", self.exchangeMusic)
			self.notif.add_action("no_dontdelete", "No", self.dismissNotif)
		self.notif.show()
