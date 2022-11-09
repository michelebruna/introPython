# 1 - Imports / Bibliotecas

# 2- Classes

# 3 - Métodos e funções (executam alguma ação. Se só faz e fica quietinho, é um método. Se tem retorno, é uma função)
# def (definition ou definição é um método ou função, não distingue os dois)

# ''' - 3 aspas simples faz comentário em bloco

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

def exibir_dia_da_semana_if(numero):
    if numero == 1:
        print('O dia é Segunda')
    if numero == 2:
        print('O dia é Terça')
    if numero == 3:
        print('O dia é Quarta')
    if numero == 4:
        print('O dia é Quinta')
    if numero == 5:
        print('O dia é Sexta')
    if numero == 6:
        print('O dia é Sábado')
    if numero == 6:
        print('O dia é Domingo')
    else:
        print('Número de dia inválido. Digite um número de 1 a 7')


'''def exibir_dia_da_semana_match(numero):
    match numero:
        case 1:
            print('O dia é Segunda')
            exit()
        case 2:
            print('O dia é Terça')
            exit()
        case 3:
            print('O dia é Quarta')
            exit()
        case 4:
            print('O dia é Quinta')
            exit()
        case 5:
            print('O dia é Sexta')
            exit()
        case 6:
            print('O dia é Sábado')
            exit()
        case 7:
            print('O dia é Domingo')
            exit()
        case _:
            print('Número de dia inválido. Digite um número de 1 a 7') '''


def brincar_de_para_ou_continua():
    resposta = 'C' # continua

    while resposta == 'C' or resposta == 'c':
        resposta = input('Digite C para continuar ou qualquer outro caracter para parar')

    print('Você decidiu parar com a brincadeira')


#Estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Michele')


    #chamar a função de cálculo da área do retângulo
    resultado = calcular_area_do_retangulo(4,3)
    print(f'A área do retângulo é de {resultado} m2')


    #chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado} m2')


    #chamar a função de cálculo da área do triângulo
    resultado = calcular_area_do_triangulo(7,4)
    print(f'A área do triângulo é de {resultado} m2')


    #executar uma contagem progressiva
    realizar_contagem_progressiva(11)


    #exibir o nome do candidato várias vezes
    apoiar_candidato('Candidato', 100)


    #brincar de plim
    brincar_de_plim(100)


    #exemplo de dia da semana com if, elif e else
    exibir_dia_da_semana_if(0)

    '''  # exenplo de dia da semana com match case
    exibir_dia_da_semana_match(1) '''

    # exemplo com while (para ou continua)
    brincar_de_para_ou_continua()