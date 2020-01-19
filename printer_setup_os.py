import os
from pprint import pprint
import json
# print(os.system('ping 10.0.0.1'))

with open('printer_config.json', 'r') as f:
    data = json.load(f)

for line in data:
    print(line, data[line])
