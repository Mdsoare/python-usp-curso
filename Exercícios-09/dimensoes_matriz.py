'''
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as 
dimensões da matriz recebida, no formato iXj.
'''

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if matriz else 0  # Verifica se a matriz não está vazia antes de obter o número de colunas
    
    print(f"{linhas}X{colunas}")

# Exemplo de uso:
minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)