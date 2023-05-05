'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para receber quatro notas, calcular e imprima a média aritmética. 
'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota:"))

rst = (n1 + n2 + n3 + n4) / 4

print(f"A média aritmética é {rst:.1f}")