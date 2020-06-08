import Arquivos
import socket


class ConvertIps:
    def __init__(self):
        print("Preparando tabela de IPs")
        self._user_hostnames = Arquivos.ler_user_hostnames()
        self._ips_locais = Arquivos.ler_ips_fixos()
        self._get_ips_das_maquinas()

    def converte_ip_local(self, ip):
        if ip in self._ips_locais:
            return self._ips_locais[ip]
        else:
            return "Desconhecido"

    def _get_ips_das_maquinas(self):
        for host in self._user_hostnames:
            try:
                ip = socket.gethostbyname(host)
                self._ips_locais[ip] = self._user_hostnames[host]
            except socket.gaierror:
                print('Erro no host '+host)
