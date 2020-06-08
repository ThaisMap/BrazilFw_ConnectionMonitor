from datetime import datetime
from msvcrt import kbhit as CatchKeybordHit

from ConverteIps import ConvertIps
from Arquivos import salvar_no_arquivo
from Scrape import get_conexoes

converter = ConvertIps()


def monitoramento_continuo():
    print("Iniciando monitoramento")
    conexoes_ativas = get_conexoes()
    cont_fechadas = 0
    loops = 0

    while True:
        try:
            conexoes_anteriores = [c for c in conexoes_ativas]
            conexoes_ativas = get_conexoes()
            ids = get_ids(conexoes_ativas)
            qtde_fechadas = save_closed_connections(conexoes_anteriores, ids)
            cont_fechadas += qtde_fechadas
            loops += 1
            print("{}: {} conexões fechadas (+ {})".format(loops, cont_fechadas, qtde_fechadas))
            if CatchKeybordHit():
                break
        except KeyboardInterrupt:
            break


def get_ids(lista_conexoes):
    ids = [x['id'] for x in lista_conexoes]
    return ids


def save_closed_connections(conexoes_anteriores, novos_ids):
    cont_fechados = 0
    for conexao in conexoes_anteriores:
        if conexao['id'] not in novos_ids:
            del conexao['id']
            conexao['fim'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S:%f')
            conexao['host_origem'] = converter.converte_ip_local(conexao['origem'])
            salvar_no_arquivo(conexao)
            cont_fechados += 1

    return cont_fechados


if __name__ == "__main__":
    monitoramento_continuo()
