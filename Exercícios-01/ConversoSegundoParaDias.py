#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Faça um programa em Python que, dada a quantidade de segundos, 
"quebre" esse valor em dias, horas, minutos e segundos. 
A saída deve estar no formato: a dias, b horas, c minutos e d segundos. 
Atualização: 18/09/2024
"""

def converter_segundos(segundos):
    """Converte uma quantidade de segundos em dias, horas, minutos e segundos.

    Args:
        segundos (int): A quantidade de segundos a ser convertida.

    Returns:
        str: Uma string formatada com o resultado da conversão.
    """

    if segundos < 0:
        return "O número de segundos deve ser positivo."

    # Cálculo das unidades de tempo
    dias = segundos // (60 * 60 * 24)
    segundos %= (60 * 60 * 24)
    horas = segundos // (60 * 60)
    segundos %= (60 * 60)
    minutos = segundos // 60
    segundos %= 60

    # Formatação da saída
    return f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos."

# Entrada do usuário
while True:
    try:
        segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
        if segundos >= 0:
            break
        else:
            print("O número de segundos deve ser positivo.")
    except ValueError:
        print("Por favor, digite um número inteiro.")

# Chamada da função e exibição do resultado
resultado = converter_segundos(segundos)
print(resultado)