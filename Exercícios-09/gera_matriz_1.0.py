'''
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa com as funções cria_matriz(num_linhas, num_colunas) e ler_matriz()
onde o usuário informará o número de linhas, colunas e valor (num laço) e por fim imprima o resultado
'''

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
print("[", end="")  # imprime o colchete de abertura da matriz
print()
for i in range(len(A)):
    print("[", end="")  # imprime o colchete de abertura de cada linha da matriz
    for j in range(len(A[i])):
        print(A[i][j], end="")
        if j < len(A[i]) - 1:
            print(", ", end="")  # imprime vírgula e espaço entre os elementos da linha
    print("]", end="")  # imprime o colchete de fechamento de cada linha da matriz
    if i < len(A) - 1:
        print(",")  # imprime uma vírgula entre as linhas
    else:
        print("")  # imprime uma nova linha após a última linha

print("]")  # imprime o colchete de fechamento da matriz
'''