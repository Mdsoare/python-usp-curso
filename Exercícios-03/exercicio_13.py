'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa que receba um número natural nn na entrada e imprima n!n! (fatorial) na saída.
'''
n = input("Digite o valor de n: ")

if not n.isdigit():
    print("Entrada inválida. Digite um número inteiro não negativo.")
else:
    n = int(n)
    if n < 0:
        print("Entrada inválida. Digite um número inteiro não negativo.")
    elif n == 0 or n == 1:
        pd = 1
        print(pd)
    else:
        fatorial = 1
        for i in range(2, n+1):
            fatorial *= i
        print(fatorial)