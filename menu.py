# 1 - Imports / Bibliotecas

# 2- Classes

# 3 - Métodos e funções (executam alguma ação. Se só faz e fica quietinho, é um método. Se tem retorno, é uma função)
# def (definition ou definição é um método ou função, não distingue os dois)


def print_hi(name):
    print(f'Hi, {name}') # f'' significa format, ele entende que o que está entre chaves é uma variável. Observado na
  #  versão 3 do Python para frente

def calcular_area_do_retangulo(largura, comprimento): #no python utiliza o snake case, com o _ entre as palavras.
    return largura * comprimento                #informar o tipo é opcional. = (recebe) e == (igual). Return é de função


def calcular_area_do_quadrado(lado):
    return lado **2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def realizar_contagem_progressiva (fim):
    for numero in range(fim): #repetir o bloco de 0 até o fim
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero <99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(f'{numero + 1}  - {nome}')


def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('Plim!')
        else:
            print('{:0>3}'.format(numero))

def sair():
    print('Obrigada e Volte Sempre')


def exibir_menu(escolha):
    opcao = {
        1: print_hi('Michele'),
        2: calcular_area_do_retangulo(8, 9),
        3: calcular_area_do_quadrado(7),
        4: calcular_area_do_triangulo(5, 4),
        5: realizar_contagem_progressiva(10),
        6: apoiar_candidato('Sábado', 10),
        7: brincar_de_plim(20),
        8: sair()
    }
    return opcao.get(escolha, 'Opção Inválida')


#Estrutura de identificação / execução do script
if __name__ == '__main__':
    continua = True

    #while continua:
    print('####################################')
    print('#                                  #')
    print('#         MENU DE OPÇÔES           #')
    print('#                                  #')
    print('#   1 - Olá Mundo                  #')
    print('#   2 - Area do Retângulo          #')
    print('#   3 - Area do Quadrado           #')
    print('#   4 - Area do Triângulo          #')
    print('#   5 - Contagem Progressiva       #')
    print('#   6 - Apoiar Candidato           #')
    print('#   7 - Brincar de Plim            #')
    print('#                                  #')
    print('#   Z - Sair                       #')
    print('#                                  #')
    print('####################################')


    escolha = input('Escolha sua opção:')
    print(f'A sua escolha foi: {escolha}')
    exibir_menu(escolha)