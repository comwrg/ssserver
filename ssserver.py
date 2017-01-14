import json
import urllib.request
import re
import subprocess
import sys



def getssinfo(containword):
    with urllib.request.urlopen('https://doub.io/sszhfx/') as h:
        html = h.read().decode('utf-8')
        pattern = '''<td>(.*?)<.*
<td>([\d|\.]*?)</td>
<td>(.*)</td>
<td>(.*)</td>
<td><a href="https://doub.io/sszhfx/" target="_blank" style="color:#5a5a5a">(.*)</a></td>'''
        #pattern = '<td width="15%">(.*)<'
        m = re.findall(pattern, html)
        configs = []
        for config in m:
            #print(config)
            #('216.189.158.147', '12422', 'dou-bi.co12422', 'chacha20')
            # if server_port is not int than continue
            if not config[2].isdigit():
                continue
            data = {
                "remarks": config[0].replace('<span style="color: #339966;"><strong>','').replace('</strong></span>','').replace('&#8211;','-'),
                'server' : config[1],
                'server_port' : config[2],
                'password' : config[3],
                'method' : config[4],
                "auth": False,
                "timeout": 5
            }
            for w in containword:
                if w in data['remarks']:
                    configs.append(data)
        #print(configs)
        return configs
    

#os.system('taskkill /im Shadowsocks.exe')

with open(file='gui-config.json',mode='r', encoding='utf-8') as f:
    data = json.load(f)
    #print(data)

print('getssinfo()')
info = getssinfo(['美国'])
if(info == ''):
    sys.exit(-1)

with open('gui-config.json','w', encoding='utf-8') as f:
    #for i in data['configs']:
    data['configs'] = info
    #data = json.loads(json.dumps(data))
    print(json.dumps(data, indent=4))
    json.dump(data, f, indent=4)

subprocess.Popen('Shadowsocks.exe')

