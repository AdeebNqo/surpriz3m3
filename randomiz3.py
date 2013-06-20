import win32api
def main():
    print("---------------------------------------------------")
    print(str(win32api.GetUserName())+" hope you enjoy the new songs!")
    print("---------------------------------------------------")
    drives = win32api.GetLogicalDriveStrings()
    
if __name__=='__main__':
    main()
