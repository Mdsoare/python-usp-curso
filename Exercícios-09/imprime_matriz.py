"""
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Função para imprimir matrizes linha por linha, sem espaços extras ao final.
Atualização: 2026-08-25
"""


def imprime_matriz(matriz: list) -> None:
    """Imprime a matriz linha por linha, omitindo espaços à direita do último elemento."""
    for linha in matriz:
        if linha:
            for elemento in linha[:-1]:
                print(elemento, end=" ")
            print(linha[-1])


if __name__ == "__main__":
    # Exemplo de uso:
    minha_matriz = [[1], [2], [3]]
    imprime_matriz(minha_matriz)
    print()
    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    imprime_matriz(minha_matriz)
    print()
    minha_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    imprime_matriz(minha_matriz)
