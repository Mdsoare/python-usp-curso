"""
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Função que verifica se duas matrizes podem ser multiplicadas.
Atualização: 2026-08-25
"""


def sao_multiplicaveis(m1: list, m2: list) -> bool:
    """Verifica se o número de colunas da primeira matriz é igual ao de linhas da segunda."""
    if not m1 or not m2 or not m1[0] or not m2[0]:
        return False
    return len(m1[0]) == len(m2)


if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print(sao_multiplicaveis(m1, m2))  # False

    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    print(sao_multiplicaveis(m1, m2))  # True
