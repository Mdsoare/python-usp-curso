#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para receber quatro notas, calcular e imprima a média aritmética.
Atualização: 18/09/2024
"""
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list): Uma lista de notas numéricas.

    Returns:
        float: A média aritmética das notas.
    """
    return sum(notas) / len(notas)

def validar_notas(notas):
    """Verifica se todas as notas estão no intervalo de 0 a 10.

    Args:
        notas (list): Uma lista de notas numéricas.

    Returns:
        bool: True se todas as notas forem válidas, False caso contrário.
    """
    return all(0 <= nota <= 10 for nota in notas)

notas = []
todas_notas_validas = True

for i in range(4):
    try:
        nota = float(input(f"Digite a {i+1}ª nota: "))
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Erro: A nota deve estar entre 0 e 10!")
            todas_notas_validas = False
            break
    except ValueError:
        print("Erro: A nota deve ser um número decimal válido!")
        todas_notas_validas = False
        break

if todas_notas_validas:
    media = calcular_media(notas)
    print(f"A média aritmética das notas é {media:.2f}.")
else:
    print("Erro: Não foi possível calcular a média. Verifique as notas informadas.")