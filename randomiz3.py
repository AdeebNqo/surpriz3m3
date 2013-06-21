import sys
import pyudev
def main():
        os = sys.platform
        if (os.find("win") != -1):
		print("Detected windows")
                #import win32api
                #username = win32api.GetUsername()
                #input("processing...")
	elif (os.find("linux") != -1):
		print("Detected linux")
		deviceDriver = pyudev.Context()
		devices = deviceDriver.list_devices()
		for device in devices:
			print("_____________")	
			print(device.sys_name)
			print(device.device_path)
if __name__=='__main__':
    main()
