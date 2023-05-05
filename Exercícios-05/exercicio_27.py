'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo nn e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros
'''

def eh_hipotenusa(n):
    for i in range(1, n):
        for j in range(1, n):
            if n == ((i**2) + (j**2))**0.5:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for i in range(1, n+1):
        if eh_hipotenusa(i):
            soma += i
    return soma

print(soma_hipotenusas(25))