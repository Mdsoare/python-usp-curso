"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais.
"""

numero = int(input("Digite um número natual: "))

try:
    if numero < 0:
        print("Erro! Digite um número natural.")
    elif numero == 0:
        print(0)
    else:
        termo = 1
        for _ in range(1, numero + 1):
            print(termo)
            termo = termo + 2
except ValueError:
    print("Erro! Digite um número natural.")
