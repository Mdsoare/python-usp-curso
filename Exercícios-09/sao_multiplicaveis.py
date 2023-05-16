'''
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro 
e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.
'''

def sao_multiplicaveis(m1, m2):
    num_colunas_m1 = len(m1[0])
    num_linhas_m2 = len(m2)

    return num_colunas_m1 == num_linhas_m2

# Exemplo de uso:
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
resultado = sao_multiplicaveis(m1, m2)
print(resultado)


m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
resultado = sao_multiplicaveis(m1, m2)
print(resultado)