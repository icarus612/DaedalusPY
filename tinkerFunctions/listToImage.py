import sys
import pandas as pd
import requests
import re
links = [i for i in pd.read_csv(sys.argv[1])]
for i in range(len(links)):
    r = requests.get(links[i])
    x = re.search(r'\.[psj][pvn].*g', links[i])
    name = f'{i}' + x.group()
    print(name)
    with open(f'./saveFile/{name}', 'wb') as f:
        f.write(r.content)