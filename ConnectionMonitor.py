import Scrape
from datetime import datetime
from ConvertIps import ConvertIps
converter = ConvertIps()

def get_ids(connections):
    ids = [x['id'] for x in connections]
    return ids


def get_closed_conections(old_connections, new_ids):
    closed = [x for x in old_connections if (x['id'] not in new_ids)]
    for x in closed:
        x['fim'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S:%f')
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
        print("Loop {}, {} closed connections".format(loops, len(closed_connections)))
    return closed_connections

def get_destiny_names(connections):
    for conn in connections:
        try:
            Scrape.test_address(conn['destino'])
        except:
            print("Failure")

def get_origin_names(connections):
    for conn in connections:
        conn['hostname'] = converter.convert_local_ip(conn['origem'])
        print(conn)


def main():
    closed_connections = monitoring_loop(3)
    print("Getting hostnames")
    get_origin_names(closed_connections)
    # for c in closed_connections:
    #     print(c)

if __name__ == "__main__":
    main()
