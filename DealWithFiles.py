import json


def read_fixed_ips():
    with open('ips.json', 'r') as f:
        ips = json.load(f)
        return ips


def read_user_hostnames():
    with open('hostnames.json', 'r') as f:
        hostnames = json.load(f)
        return hostnames


def write_connections_to_file(connections):
    with open('closed.json', 'a') as f:
        f.write(json.dumps(connections, indent=4))


def read_authorization_header():
    with open('auth.json', 'r') as f:
        header = json.load(f)
    return header
