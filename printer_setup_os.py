#! /usr/bin/env python3
from telnetlib import Telnet
import sys
from pprint import pprint
import json

support = "support-contact testingAgain"
xit = "exit"
reply = "Y"
host = "10.0.107.22"
with open('printer_configs.json', 'r') as f:
    data = json.load(f)
print('I have the config file.\n')


print(f'Attempting to connect {host}... \n')
tn = Telnet(host=host, port=23, timeout=5)
print(tn.read_until(b'\r\nType "help or ?" for information.\r\n>', timeout=10))
print(f"Connected to {host} \n")
tn.write(support.encode('ascii') + b"\r\n")
tn.write(xit.encode('ascii') + b"\r\n")
tn.write(reply.encode('ascii') + b"\r\n")


# for i in data:
#     tn.write({data[i]} {i}").encode("ascii") + b"\r\n"

output = tn.read_very_eager()
print(output)
tn.close()
print('Done')
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
