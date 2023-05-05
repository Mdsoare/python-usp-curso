'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais.
'''
n = int(input("Digite o valor de n: "))

try:
    if (n < 0 ):
        print("Erro! Digite um número natural.")
    elif (n == 0):
        print(0)
    else:
        r = 1
        for i in range(1, n+1):
            print(r)
            r = (r+2)
except ValueError:
    print("Erro! Digite um número natural.")