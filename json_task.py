import json
from tabulate import tabulate

# reading json file
with open('sample-data.json', 'r') as f:
    data = json.load(f)

# preparing list
keys = ["dn", "descr", "speed", "mtu"]

arr = []

for obj in data["imdata"]:
    attr = obj["l1PhysIf"]["attributes"]
    tmp = []
    for i in keys:
        tmp.append(attr.get(i))
    arr.append(tmp)

header_keys = ["DN", "Description", "Speed", "MTU"]


# printing
print("Interface Status")
width = 67
print("=" * width)
print(tabulate(arr, headers=header_keys))
