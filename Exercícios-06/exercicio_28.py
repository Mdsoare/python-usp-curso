'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, 
verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista 
correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista).
'''

def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))  # remove elementos repetidos
    lista_sem_repeticao.sort()  # ordena a lista resultante
    return lista_sem_repeticao

lista1 = [3, 2, 1, 2, 4, 5, 6, 5, 4, 7, 8, 1]
print(remove_repetidos(lista1)) # Imprime [1, 2, 3, 4, 5, 6, 7, 8]

lista2 = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista2)) # Imprime [1, 2, 3, 4]

print(remove_repetidos([1, 2, 3, 3, 3, 4])) # Imprime [1, 2, 3, 4]