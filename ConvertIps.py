import DealWithFiles
import socket


class ConvertIps:
    def __init__(self):
        print("Preparando tabela de IPs")
        self._user_hostnames = DealWithFiles.read_user_hostnames()
        self._local_ips = DealWithFiles.read_fixed_ips()
        self._get_user_ips()

    def convert_local_ip(self, ip):
        if ip in self._local_ips:
            return self._local_ips[ip]
        else:
            return "Desconhecido"

    def _get_user_ips(self):
        for host in self._user_hostnames:
            try:
                ip = socket.gethostbyname(host)
                self._local_ips[ip] = self._user_hostnames[host]
            except socket.gaierror:
                print('Erro no host '+host)
