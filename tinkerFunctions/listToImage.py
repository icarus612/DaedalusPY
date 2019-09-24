import sys
import pandas as pd
import requests
import re
import os
links = [i for i in pd.read_csv(sys.argv[1])]
place = sys.argv[2] if len(sys.argv) >= 3 else "./saveFile"
try:
    os.mkdir(place)
except FileExistsError:
    pass
for i in range(len(links)):
    req = requests.get(links[i])
    x = re.search(r'\.[psj][pvn].*g', links[i])
    name = f'{i}' + x.group()
    print("saving " + name)
    with open(f'{place}/{name}', 'wb') as file:
        file.write(req.content)

