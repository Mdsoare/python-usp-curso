'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
'''

def n_primos(n):
    qtd_primos = 0  # inicializa a contagem de primos
    
    for num in range(2, n+1):
        eh_primo = True  # assume que num é primo
        
        for div in range(2, int(num**(1/2))+1):
            if num % div == 0:
                eh_primo = False
                break
        
        if eh_primo:
            qtd_primos += 1
    
    return qtd_primos

# Testes
print(n_primos(2))   # Imprime 1
print(n_primos(4))   # Imprime 2
print(n_primos(121)) # Imprime 30