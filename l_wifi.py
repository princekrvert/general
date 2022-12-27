#!/usr/bin/python3
import subprocess
import re
import os
#this script is made by prince kumar 
wifi_name = subprocess.check_output(["ls","/etc/NetworkManager/system-connections"]).decode()
names = re.findall(r"(.*)\n",wifi_name)
for name in names:
    wifi_row = subprocess.check_output(["sudo","cat",f"/etc/NetworkManager/system-connections/{name}"]).decode()
    ssid = re.findall(f"ssid=(.*)\n",wifi_row)
    password = re.findall(f"psk=(.*)\n",wifi_row)
    print(ssid)
    print(password)
    with open("wifi.txt","a") as f:
        f.write(f"{ssid} : {password}\n")
        f.close()

