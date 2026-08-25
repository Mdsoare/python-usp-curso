"""
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Função para somar duas matrizes de dimensões compatíveis.
Atualização: 2026-08-25
"""


def soma_matrizes(m1: list, m2: list):
    """Soma duas matrizes se tiverem dimensões iguais, caso contrário retorna False."""
    if not m1 or not m2 or len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]


if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(m1, m2))

    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(m1, m2))
    