import csv
import json
import os
from datetime import datetime


def ler_ips_fixos():
    with open('ips.json', 'r') as arquivo:
        ips = json.load(arquivo)
        return ips


def ler_user_hostnames():
    with open('hostnames.json', 'r') as arquivo:
        hostnames = json.load(arquivo)
        return hostnames


def ler_cabecalho_autorizacao():
    with open('auth.json', 'r') as arquivo:
        cabecalho = json.load(arquivo)
    return cabecalho


def escrever_cabecalho_csv(fieldnames, filename):
    with open(filename, 'a', newline='') as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()


def salvar_no_arquivo(conexao):
    nome_arquivo = 'logs/closed {}h.csv'.format(datetime.now().strftime('%Y-%m-%d %H'))
    colunas = conexao.keys()

    if not os.path.exists(nome_arquivo):
        escrever_cabecalho_csv(colunas, nome_arquivo)

    with open(nome_arquivo, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas, delimiter=';')
        writer.writerow(conexao)


