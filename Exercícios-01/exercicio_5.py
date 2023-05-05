'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
'''
numero = int(input("Digite um número inteiro: "))

dezenas = (numero // 10) % 10

print(f"O dígito das dezenas é {dezenas}")