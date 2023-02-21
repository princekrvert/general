#!/usr/bin/env python3
import argparse
import regx 
parser = argparse.ArgumentParser(description="Mac changer for linux ")
parser.add_argument("-i","--interface", help="Name of the interface",required="True")
args = parser.parse_args()
# open the mac file nad read the company macs 
def mac(_type):
    if _type = wireless:
        with open("mac.txt",'r') as f:
            print(f)
