'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. 
'''
segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

segundos_restantes = (segundos % 60)
minutos = (segundos // 60)
minutos_restantes = (minutos % 60)
horas = (minutos // 60)
horas_restantes = (horas % 24)
dias = (horas // 24)

print(f"{dias} dias, {horas_restantes} horas, {minutos_restantes} minutos e {segundos_restantes} segundos.")