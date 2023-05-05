'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
'''
while True:
    num = input("Digite um número inteiro positivo: ")

    if not num.isdigit():
        print("Entrada inválida! Digite apenas números inteiros positivos.")
        continue

    if int(num) <= 0:
        print("Entrada inválida! Digite apenas números inteiros positivos.")
        continue

    break

soma = 0

for digito in num:
    soma += int(digito)

print(f"A soma dos dígitos de {num} é {soma}.")