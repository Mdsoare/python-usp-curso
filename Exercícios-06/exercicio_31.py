'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa que recebe uma sequência de números inteiros 
e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. 
Note que 0 (ZERO) não deve fazer parte da sequência.
'''

numeros = []
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    numeros.append(num)

print("\n")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])