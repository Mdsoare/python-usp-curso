'''
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa com as funções cria_matriz(num_linhas, num_colunas) e ler_matriz()
onde o usuário informará o número de linhas, colunas e valor (num laço) e por fim imprima o resultado
OBS: A saída foi alterada com o uso da função pprint()
'''

from pprint import pprint

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz
    
def ler_matriz():
    lin = int(input("Digite o numero de linhas: "))
    col = int(input("Digite o numero de colunas: "))
    return cria_matriz(lin, col)

A = ler_matriz()
pprint(A)