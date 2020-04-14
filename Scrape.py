from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
import socket

def get_connections():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    url = 'https://192.168.0.5:8181/connection-monitor.php'
    headers = {'authorization': 'Basic cm9vdDpiclQxMDEyKg=='}
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.select('table.listview-1 > tbody > tr')
    connections = []
    for row in rows:
        cell = row.find_all('th')
        origin = cell[2].string
        target = cell[3].string
        service = cell[6].string
        local_ip = "192.168.0"
        if origin[0:9] == local_ip and target[0:9] != local_ip and (service == 'http' or service == 'https'):
            conn = {'id': origin+target,
                    'origem': origin,
                    'destino': target,
                    'servico': service,
                    'inicio': datetime.now().strftime('%d-%m-%Y %H:%M:%S:%f')}
            connections.append(conn)
    return connections

def test_address(ip):
    r = requests.get(ip, verify=False)
    print(r.status_code)

if __name__ == "__main__":
    get_connections()
