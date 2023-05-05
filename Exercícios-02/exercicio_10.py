'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Receba 3 números inteiros na entrada e imprima crescente se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente
'''

import re

entrada = input("Digite três numeros: ")
match = re.match(r"\((-?\d+),\s*(-?\d+),\s*(-?\d+)\)", entrada)

if match:
    try:
        n1, n2, n3 = map(int, match.groups())
        if n1 < n2 < n3:
            print("crescente")
        else:
            print("não está em ordem crescente")
    except ValueError:
        print("Entrada inválida.")
else:
    print("Entrada inválida.")
