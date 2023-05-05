'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
'''

def is_vogal(vogal):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if vogal.lower() in vogais:
        return True
    else:
        return False

print(is_vogal('A')) # imprime True
print(is_vogal('B')) # imprime False
