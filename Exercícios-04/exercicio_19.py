"""
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
"""


def is_prime(number):
    """Verifica se um número é primo."""
    if number < 2:
        return False
    for contador in range(2, int(number**0.5) + 1):
        if number % contador == 0:
            return False
    return True


def largest_prime(number):
    """Retorna o maior número primo menor ou igual a um número dado."""
    if not isinstance(number, int) or number < 2:
        raise ValueError("O número deve ser um inteiro maior ou igual a 2.")

    for contador in range(number, 1, -1):
        if is_prime(contador):
            return contador

    raise ValueError("Nenhum número primo encontrado no intervalo.")


try:
    num = int(input("Digite um número inteiro maior ou igual a 2: "))
    print(f'O maior número primo menor ou igual a "{num}" é: {largest_prime(num)}')
except ValueError as error:
    print(f"Erro: {error}")
