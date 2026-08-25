"""Data: 16/05/2023.

Autor: Marcelo Soares
Descrição: Escreva um programa com as funções cria_matriz(num_linhas, num_colunas) e ler_matriz()
onde o usuário informará o número de linhas, colunas e valor (em um laço) e por fim imprima o resultado.
"""


def cria_matriz(num_linhas, num_colunas):
    """Cria e preenche uma matriz com base nas dimensões especificadas."""
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def ler_matriz():
    """Lê as dimensões da matriz informadas pelo usuário e inicia a criação."""
    lin = int(input("Digite o numero de linhas: "))
    col = int(input("Digite o numero de colunas: "))
    return cria_matriz(lin, col)


def main():
    """Executa a leitura e a formatação de saída da matriz."""
    matriz_a = ler_matriz()

    print("[")
    for i, linha in enumerate(matriz_a):
        print("[", end="")
        for j, elemento in enumerate(linha):
            print(elemento, end="")
            if j < len(linha) - 1:
                print(", ", end="")
        print("]", end="")
        if i < len(matriz_a) - 1:
            print(",")
        else:
            print("")
    print("]")


if __name__ == "__main__":
    main()
