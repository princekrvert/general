#!/usr/bin/env python3
# made by prince kumar 
# date 13 apr 2023
# all import goes here 
import requests 
import argparse
from pprint import pprint
import time 
import json 
# initilize the parser 

parser = argparse.ArgumentParser(description='Mass ip locater')
parser.add_argument("-f","--file",help='Enter the file name to read from ')
parser.add_argument('-o',"--output",help="Output file name" )
args = parser.parse_args()
# Make a function to track the ip
def getlocation(ip):
    base_url = "http://ip-api.com/json"
    req = requests.get(f"{base_url}/{ip}")
    if req.status_code == 200:
        return req.json()
    elif req.status_code == 429:
        print("Excedded the limit , Please wait for a minute..")
    else:
        print("somtheing wrong occured , Please check your input file") 
# now read for conditon 
if(args.file != None):
    # now read the files 
    with open(args.file,"r") as f:
        # create a variabe to track the number of requests 
        i = 0 
        for ip in f.readlines():
            if( i == 44):
                #then  wait for a minute ..
                time.sleep(60000)
                #and reset the i 
                i = 0 
            else:
                json_data = getlocation(ip.replace("\n",""))
                i+=1
                #check for output file 
                if(args.output != None):
                    with open(args.output,"a") as o_file:
                        o_file.write(json.dumps(json_data))
                        o_file.write("\n")
                        pprint(json_data)
                else:
                    #simply print the output
                    pprint(json_data)
else:
    print("\033[31;1m input file is not defined ")

            

    
