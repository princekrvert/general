import time
import os 
import subprocess
import re
#this script is mada by prince kumar 
all_o = subprocess.check_output(["netsh","wlan","show","profile"]).decode()
profile_names_row =(re.findall("All User Profile     : (.*)\r",(all_o)))
#print(all_o)
if len(profile_names_row) != 0:
	for name in profile_names_row:
		wifi_name ={}
		ispassraw = subprocess.check_output(["netsh","wlan","show","profile", name]).decode()
		if re.search("Security key           : Absent", ispassraw):
			continue
		else:
			wifi_name["ssid or name"] = name 
			wifipass = subprocess.check_output(["netsh","wlan","show","profile", name, "key=clear"]).decode()
			has_pass = re.search("Key Content            : (.*)\r", wifipass)
			if has_pass == None:
				wifi_name[password] = None
			else:
				print(f'{wifi_name} : password {has_pass[1]}')
				with open("wifiinfo.txt",'a') as f:
					f.write(f"{name} :: {has_pass[1]}\n")
					f.close()


		