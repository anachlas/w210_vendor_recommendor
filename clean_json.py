import sys
import json

with open(sys.argv[1], 'r') as f:
    contents = f.read()

data = []
for line in contents.splitlines():
    vendor = json.loads(line)
    vendor["dunsnumber"] = vendor["dunsnumber"].zfill(9)
    data.append(vendor)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, indent=0)
