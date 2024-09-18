#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para receber dados fictícios para simular uma fatura
Atualização: 18/09/2024
"""

def validar_data(dia, mes):
    """Valida se a data é válida."""
    meses_31 = [1, 3, 5, 7, 8, 10, 12]
    meses_30 = [4, 6, 9, 11]
    if mes not in range(1, 13):
        return False
    if mes in meses_31 and 1 <= dia <= 31:
        return True
    elif mes in meses_30 and 1 <= dia <= 30:
        return True
    elif mes == 2 and 1 <= dia <= 28:  # Considerando ano não bissexto
        return True
    return False

nome = input("Digite o nome do cliente: ")
while True:
    try:
        dia = int(input("Digite o dia de vencimento: "))
        mes = int(input("Digite o mês de vencimento: "))
        if validar_data(dia, mes):
            break
        else:
            print("Data inválida. Por favor, digite novamente.")
    except ValueError:
        print("Digite um número válido para o dia e o mês.")

try:
    valor = float(input("Digite o valor da fatura: "))
except ValueError:
    print("Digite um valor numérico para a fatura.")

print(f"Olá, {nome}")
print(f"Sua fatura com vencimento em {dia}/{mes} no valor de R$ {valor:.2f} está fechada.")