'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros 
e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
'''

def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

lista = [1, 2, 3, 4, 5]
print(soma_elementos(lista)) # Imprime 15