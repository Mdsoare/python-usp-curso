'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
'''

def maior_elemento(lista):
    maior = lista[0]  # inicializa o maior valor como o primeiro elemento da lista
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

lista = [1, 5, 3, 2, 4]
print(maior_elemento(lista)) # Imprime 5