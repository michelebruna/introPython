# 1 - Importação de pacotes
import json
import pytest


# 2 - Classe


# 3 - Definições (Funções e Métodos)

dados = {}

dados['cliente'] = [] # indica a criação de um vetor, matriz, lista...
dados['cliente'].append({  #  O append insere um registro após o último elemento, ou seja, ele é útil quando é preciso colocar o novo registro na última posição da tabela.
    'nome':'Michele',
    'telefone':'37999999999',
    'email':'michele@iterasys.com.br'
})

dados['cliente'].append({
    'nome':'Ana',
    'telefone':'31999999999',
    'email':'ana@iterasys.com.br'
})

def criar_json():
    with open('clientes.json','w') as outfile: # w é de write, r de read...
        json.dump(dados, outfile, indent=4)

def ler_json():
    with open('clientes2.json') as outfile:
        dados = json.load(outfile)
        for registro in dados['cliente']:
            print('nome: ' + registro['nome'])
            print('telefone: ' + registro['telefone'])
            print('email: ' + registro['email'])
            print('')

def ler_e_adicionar_json():
    with open('clientes2.json') as outfile:
        dados2 = json.load(outfile)
        #v = ','
        temp = []
        for registro in dados2['cliente']:
            # Exibir no console
            print('nome: ' + registro['nome'])
            print('telefone: ' + registro['telefone'])
            print('email: ' + registro['email'])
            print('')

            # Salvar na lista
            temp.append(
                '{\'nome\'' + ':' + '\'' + registro['nome'] +  '\',' \
                + '\'telefone\'' + ':' +  '\'' + registro['telefone'] + '\',' \
                + '\'email\'' + ':' + '\'' + registro['email'] + '\'}'
            )


            #dados['cliente'].extend(temp)
            dados['cliente'].append(temp)
        with open('clientes3.json', 'w') as outfile:  # w é de write, r de read...
            json.dump(dados, outfile,sort_keys=True,indent=4)


def testar_criar_json():
    criar_json()
    print(dados['cliente'])

def testar_ler_json():
    print('Leitura do JSON por linha / campo')
    ler_json()
    print(dados['cliente'])

def testar_ler_e_adicionar_json():
    ler_e_adicionar_json()
    print('Lista atualizada Final')
    print(dados['cliente'])

