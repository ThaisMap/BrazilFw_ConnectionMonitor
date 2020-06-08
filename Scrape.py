from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
from Arquivos import ler_cabecalho_autorizacao
import requests

def get_conexoes():
    linhas = pegar_dados_da_tabela()
    conexoes = []

    for row in linhas:
        cell = row.find_all('th')
        origin = cell[2].string
        target = cell[3].string
        service = cell[6].string
        conn = {'id': origin+target,
                'origem': origin,
                'destino': target,
                'servico': service,
                'inicio': datetime.now().strftime('%d-%m-%Y %H:%M:%S:%f')}
        if deve_considerar(conn):
            conexoes.append(conn)
    return conexoes

def deve_considerar(conexao):
    local_ip = "192.168.0"
    origem_local = conexao['origem'][:9] == local_ip
    destino_externo = conexao['destino'][:9] != local_ip
    if conexao['servico'] is not None:
        servico_web = conexao['servico'][:4] == 'http'
    else:
        servico_web = False

    return origem_local and destino_externo and servico_web


def pegar_dados_da_tabela():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    url = 'https://192.168.0.5:8181/connection-monitor.php'
    headers = ler_cabecalho_autorizacao()
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.select('table.listview-1 > tbody > tr')
    return rows


if __name__ == "__main__":
    get_conexoes()
