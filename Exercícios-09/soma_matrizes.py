'''
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz 
que represente sua soma caso as matrizes tenham dimensões iguais. 
Caso contrário, a função deve devolver False.
'''
def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    soma = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            elemento = m1[i][j] + m2[i][j]
            linha.append(elemento)
        soma.append(linha)
    
    return soma

# Exemplo de uso:
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
resultado = soma_matrizes(m1, m2)
print(resultado)


m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
resultado = soma_matrizes(m1, m2)
print(resultado)