#!/usr/bin/env python3
import argparse
import re
import subprocess
import random 
parser = argparse.ArgumentParser(description="Mac changer for linux ")
parser.add_argument("-i","--interface", help="Name of the interface",required="True")
#parser.add_argument("-c","--custom", help="Set a desire mac address",)
args = parser.parse_args()
#create a function that return a random hex value 
def random_hex():
    hex_digit = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    return random.choice(hex_digit)
# open the mac file nad read the company macs 
def mac(_type):
    if (_type == "wlo1" or _type == "wlan0"):
        with open("mac.txt",'r') as f:
            srting_mac = str(f.readlines())
            s_mac = re.findall(r"\d\d:\d\d:\d\d",srting_mac)
            cname = random.choice(s_mac)
            return cname
    else:
         with open("mac.txt",'r') as f:
            srting_mac = str(f.readlines())
            s_mac = re.findall(r"[a-z][a-z|0-9]:[a-z|0-9][a-z|0-9]:[a-z|0-9][a-z|0-9]",srting_mac)
            c_name = random.choice(s_mac)
            return c_name
# make a function that return full mac 
def full_mac(t):
    # first add the company name 
    return mac(t)+":"+random_hex()+random_hex()+":"+random_hex()+random_hex()+":"+random_hex()+random_hex()
# now change the mac three times 
p_mac = subprocess.check_output(["macchanger","-s",args.interface])
# now mac a function to change the mac 
def c_mac():
    o=subprocess.check_output(["sudo","ifconfig",args.interface,"down"])
    mac_c = subprocess.check_output(["sudo","macchanger","-m",full_mac(args.interface),args.interface])
    subprocess.run(["sudo","ifconfig",args.interface,"up"])
    return mac_c
#if (args.custom == None):
c_mac()
c_mac()
print(c_mac().decode())
