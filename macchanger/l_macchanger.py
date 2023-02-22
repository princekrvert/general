#!/usr/bin/env python3
import argparse
import re
import random 
parser = argparse.ArgumentParser(description="Mac changer for linux ")
parser.add_argument("-i","--interface", help="Name of the interface",required="True")
args = parser.parse_args()
#create a function that return a random hex value 
def random_hex():
    hex_digit = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    return random.choice(hex_digit)
# open the mac file nad read the company macs 
def mac(_type):
    if (_type == "wireless"):
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
    return mac("wireless")+":"+random_hex()+random_hex()+":"+random_hex()+random_hex()+":"+random_hex()+random_hex()
print(full_mac("kala"))
