#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
Atualização: 18/09/2024
"""

def obter_digito_dezenas(numero):
    """Obtém o dígito das dezenas de um número inteiro.

    Args:
        numero (int): O número inteiro.

    Returns:
        int: O dígito das dezenas, ou None se o número tiver menos de dois dígitos.
    """

    if numero < 0:
        numero = -numero  # Trabalhar com o valor absoluto
    if numero < 10:
        return None  # Números de um dígito não têm dezena
    return (numero // 10) % 10

# Entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Chamada da função e exibição do resultado
resultado = obter_digito_dezenas(numero)
if resultado is None:
    print("O número digitado não possui dígito das dezenas.")
else:
    print(f"O dígito das dezenas é {resultado}")