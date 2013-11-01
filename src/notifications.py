#
# Z. Mahlaza
# Class for notifying when device  detected
#
import pynotify
class notification:
	#
	# Notification types
	#
	info = "dialog-information"
	
	def __init__(self, deviceName):
		self.title = "Music exchange"
		self.deviceName = deviceName
	def notify(self, msg, notif_type, actions):
		pynotify.init(self.title)
		self.notif = pynotify.Notification(self.deviceName+" has been connected", msg, )
		if (actions.activated):
			self.notif.add_action("action_delete", "Yes", actions.funclist['yes'])
			self.notif.add_action("no_dontdelete", "No", actions.funclist['no'])
		self.notif.show()
