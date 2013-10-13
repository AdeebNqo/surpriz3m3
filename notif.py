#
# Z. Mahlaza
# Class for notifying when device  detected
#
import pynotify
class notif:
	def __init__(self, devicePath, deviceName):
		self.title = "Music exchange"
		self.deviceName = deviceName
	def notify(self, deviceName):
		pynotify.init(self.title)
		self.notif = pynotify.Notification("Connected "+self.deviceName, "Do you wish to exchange music?", "dialog-information")
		self.notif.add_action("action_delete", "Exchange Music", self.exchangeMusic)
		self.notif.add_action("no_dontdelete", "Dismiss", self.dismissNotif)
		self.notif.show()
	def exchangeMusic(self):
		print("exchanging music...")
	def dismissNotif(self):
		print("dismissing notif...")
