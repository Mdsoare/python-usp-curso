'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: escreva um programa que calcula as raízes de uma equação do segundo grau.
'''

import math

# Recebe os valores de a, b e c do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = (-b + math.sqrt(delta)) / (2 * a)
    print(f"a raiz desta equação é {raiz:.2f}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 < raiz2:
        print(f"as raízes da equação são {raiz1:.2f} e {raiz2:.2f}")
    else:
        print(f"as raízes da equação são {raiz2:.2f} e {raiz1:.2f}")