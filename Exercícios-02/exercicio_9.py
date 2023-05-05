'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Receba um número inteiro na entrada e imprima FizzBuzz se o número for divisível por 3 e 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

numero = int(input(" Digite um número inteiro: "))

if (numero % 3 == 0 and numero % 5 == 0):
    print("FizzBuzz")
else:
    print(numero)