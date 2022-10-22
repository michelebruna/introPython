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
    apoiar_candidato('Bolsonaro', 100)


    #brincar de plim
    brincar_de_plim(100)
