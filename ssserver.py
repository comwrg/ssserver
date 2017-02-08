import json
import subprocess
import sys
from core import *




# os.system('taskkill /im Shadowsocks.exe')

with open(file='gui-config.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
    # print(data)

print('getssinfo()')
info = getssinfo()
if (info == ''):
    sys.exit(-1)

with open('gui-config.json', 'w', encoding='utf-8') as f:
    # for i in data['configs']:
    data['configs'] = info
    # data = json.loads(json.dumps(data))
    print(json.dumps(data, indent=4))
    json.dump(data, f, indent=4)

subprocess.Popen('Shadowsocks.exe')
