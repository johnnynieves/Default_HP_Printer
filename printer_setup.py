#! /usr/bin/env python3
from getpass import getpass
from telnetlib import Telnet


HOST = "10.0.0.109"
user = input("Username ")
password = getpass("Password ")


with open("setup.txt","r") as f:
    config = f.readlines()
with Telnet(host=HOST) as tn:    
    for line in config:
        #print(line)
        tn.write(line.encode('ascii'))
    print(tn.read_all().decode('ascii'))

 