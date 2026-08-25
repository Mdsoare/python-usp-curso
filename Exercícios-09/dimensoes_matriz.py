"""
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Função que imprime as dimensões de uma matriz no formato iXj.
Atualização: 2026-08-25
"""


def dimensoes(matriz: list) -> None:
    """Imprime as dimensões da matriz recebida no formato LinhasXColunas."""
    linhas = len(matriz)
    colunas = len(matriz[0]) if matriz and matriz[0] else 0
    print(f"{linhas}X{colunas}")


if __name__ == "__main__":
    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)

    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    dimensoes(minha_matriz)