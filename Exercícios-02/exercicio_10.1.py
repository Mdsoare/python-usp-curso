"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Receba 3 números inteiros na entrada e imprima crescente se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente
"""

entrada = input("Digite: ")
if entrada[0] != "(" or entrada[-1] != ")":
    print("Formato de entrada inválido. Use (n1, n2, n3)")
else:
    n1, n2, n3 = map(int, entrada[1:-1].split(","))
    if n1 < n2 < n3:
        print("crescente")
    else:
        print("não está em ordem crescente")
