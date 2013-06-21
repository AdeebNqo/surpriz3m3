import sys
import pyudev
import os
def main():
        os_type = sys.platform
        if (os_type.find("win") != -1):
		print("Detected windows")
                #import win32api
                #username = win32api.GetUsername()
                #input("processing...")
	elif (os_type.find("linux") != -1):
		print("Detected linux...")
		deviceDriver = pyudev.Context()
		devices = deviceDriver.list_devices(MAJOR=8)
		count = 0

		disk_devices = [];
		for device in devices:
			path = device.device_path
			if ("usb1" in path):
				print("\t("+str(count+1)+") "+ device.sys_name)
				count = count+1
				disk_devices.append(device)
		option = input("choose phone: ")
		print("Option "+str(option)+" it is then.")
		print("path of chosen device is "+disk_devices[option-1].sys_name)
		f = open("/dev/"+disk_devices[option-1].sys_name,"r")
		print(f.readlines())
if __name__=='__main__':
    main()
