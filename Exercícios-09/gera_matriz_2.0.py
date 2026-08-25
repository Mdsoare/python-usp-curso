"""
Data: 16/05/2023
Autor: Marcelo Soares
Descrição: Programa com funções para criar e ler matrizes informadas pelo usuário,
           garantindo validação de entrada e tratamento robusto de dados.
Atualização: 2026-08-25
"""

from pprint import pprint


def cria_matriz(num_linhas: int, num_colunas: int) -> list:
    """Cria e preenche uma matriz com base nas dimensões especificadas."""
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            while True:
                try:
                    valor = int(input(f"Digite o elemento [{i}][{j}]: "))
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            linha.append(valor)
        matriz.append(linha)
    return matriz


def ler_matriz() -> list:
    """Lê as dimensões da matriz informadas pelo usuário com validação."""
    while True:
        try:
            lin = int(input("Digite o número de linhas: "))
            col = int(input("Digite o número de colunas: "))
            if lin > 0 and col > 0:
                break
            print("As dimensões devem ser maiores que zero.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")
    return cria_matriz(lin, col)


def main():
    """Função principal de execução."""
    matriz_a = ler_matriz()
    pprint(matriz_a)


if __name__ == "__main__":
    main()
