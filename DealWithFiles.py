import json

def read_fixed_ips():
    with open('ips.json', 'r') as f:
        ips = json.load(f)
        return ips


def read_user_hostnames():
    with open('hostnames.json', 'r') as f:
        hostnames = json.load(f)
        return hostnames

import socket
for ip in range(50, 255):
    this_ip = '192.168.0.'+str(ip)
    conhecidos = read_fixed_ips()
    try:
        if this_ip not in conhecidos:
            host = socket.gethostbyaddr(this_ip)[0].split('.')[0]
            print('"'+this_ip+'":"'+host+'"')
    except:
        host = "não encontrado"