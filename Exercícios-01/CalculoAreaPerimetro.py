#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para calculo de perímetro e área de um quadrado
Atualização: 18/09/2024
"""

def calcular_quadrado(lado):
    """Calcula o perímetro e a área de um quadrado.

    Args:
        lado (int): Comprimento de um lado do quadrado.

    Returns:
        tuple: Uma tupla contendo o perímetro e a área do quadrado, nessa ordem.
    """
    perimetro = lado * 4
    area = lado ** 2
    return perimetro, area

try:
    lado = int(input("Digite o valor correspondente ao lado de um quadrado: "))
    if lado <= 0:
        print("O valor digitado deve ser um número inteiro positivo maior que zero!")
    else:
        perimetro, area = calcular_quadrado(lado)
        print(f"Para um quadrado de lado {lado}:")
        print(f"O perímetro é {perimetro} e a área é {area}.")
except ValueError:
    print("Erro: Você deve digitar um número inteiro para o lado do quadrado!")