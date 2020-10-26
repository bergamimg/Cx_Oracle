import cx_Oracle
import os

arquivo = open(r'C:\Users\automacao\snow.txt','r')

username = 'nome_user'
password = 'senha'
server = 'nome_server'
banco = 'nome_banco'

for linha in arquivo:
    ordem = linha.split(';')
    os.chdir(r'C:\Users\Downloads\instantclient_19_8_windows.x32\instantclient_19_8_windows.x32')
    conn_oracle = cx_Oracle.connect(username+'/'+password+'/'+server+'/'+banco) # con = cx_Oracle.connect('username/password@server/banco')
    cursor = conn_oracle.cursor()
    query = '''UPDATE Tabela Set email = :1 Where cod_fornecedor = :2'''
    cursor.execute(query, (ordem[4], 'teste'))
    conn_oracle.commit()
conn_oracle.close()
