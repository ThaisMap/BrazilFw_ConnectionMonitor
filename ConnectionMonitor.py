import Scrape
from datetime import datetime
import DealWithFiles
from ConvertIps import ConvertIps
converter = ConvertIps()

def get_ids(connections):
    ids = [x['id'] for x in connections]
    return ids


def get_closed_conections(old_connections, new_ids):
    closed = [x for x in old_connections if (x['id'] not in new_ids)]
    for conn in closed:
        del conn['id']
        conn['fim'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S:%f')
        conn['host_origem'] = converter.convert_local_ip(conn['origem'])
    return closed


def monitoring_loop(loops_to_perform):
    loops = 0
    active_connections = Scrape.get_connections()
    closed_connections = []
    while loops < loops_to_perform:
        old_conn = [x for x in active_connections]
        active_connections = Scrape.get_connections()
        ids = get_ids(active_connections)
        closed_connections.extend(get_closed_conections(old_conn, ids))
        loops += 1
        print("Loop {}: {} closed connections".format(loops, len(closed_connections)))
    return closed_connections


def endless_monitoring():
    active_connections = Scrape.get_connections()
    closed_connections = []
    loops = 0
    while True:
        old_conn = [x for x in active_connections]
        active_connections = Scrape.get_connections()
        ids = get_ids(active_connections)
        new_closed = get_closed_conections(old_conn, ids)
        closed_connections.extend(new_closed)
        DealWithFiles.write_connections_to_file(new_closed)
        loops += 1
        print("Loop {}: {} closed connections".format(loops, len(closed_connections)))

def main():
    print("Iniciando monitoramento")
    closed_connections = monitoring_loop(5)
    print("Escrevendo em arquivo")
    DealWithFiles.write_connections_to_file(closed_connections)

if __name__ == "__main__":
    main()
