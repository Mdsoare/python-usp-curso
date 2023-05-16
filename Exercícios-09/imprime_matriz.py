'''
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Escreva uma função imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a matriz, 
linha por linha. Note que NÃO se deve imprimir espaços após o último elemento de cada linha!
'''

def imprime_matriz(matriz):
    for linha in matriz:
        for elemento in linha[:-1]:
            print(elemento, end=" ")
        print(linha[-1], end="\n")

# Exemplo de uso:
minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
print("\n")
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
print("\n")
minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
imprime_matriz(minha_matriz)