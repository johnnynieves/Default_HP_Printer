#! /usr/bin/env python3.7
from telnetlib import Telnet
import os
from pprint import pprint
import json

# print(os.system('ping 10.0.0.1'))
host = "164.248.27.80"
with open('printer_configs.json', 'r') as f:
    data = json.load(f)
print('I have the config file.\n')


print(f'Attempting to connect {host}... \n')
tn = Telnet(host=host, port=23, timeout=5)
tn.read_until(b"> ", timeout=10)

# os.system(f'telnet {host}')
print(f"Connected to {host} \n")
print('Getting current configs \n')
tn.write(b"support-contact mytest \r\n")
tn.write(b"save \r\n")
for i in data:
    tn.write({data[i]} {i}").encode("ascii") + b"\r\n"

tn.write(b"save \r\n")
print('EOF')
# os.system('/ \n')
# os.system('support-contact test')
# os.system('exit')


# print('passing config\n')
# tn.write(data.encode('ascii'))
# print(tn.read_all().decode('ascii'))
# print('Exiting\n')
# tn.write(b"exit\n")

# for line in data:
#     # os.subsystem(data[line], line)
#
# print(tn.read_all().decode('ascii'))
