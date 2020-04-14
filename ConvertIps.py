import DealWithFiles
import socket

class ConvertIps:
    def __init__(self):
        self._user_hostnames = DealWithFiles.read_user_hostnames()
        self._fixed_ips = DealWithFiles.read_fixed_ips()

    def convert_local_ip(self, ip):
        if ip in self._fixed_ips:
            return self._fixed_ips[ip]

        try:
            # de ('ERBN01.rodominas.local', [], ['192.168.0.59']) para 'ERBN01'
            hostname = socket.gethostbyaddr(ip)[0].split('.')[0]
            username = self._user_hostnames.get(hostname, "Desconhecido")
            return username
        except:
            return "Desconhecido"