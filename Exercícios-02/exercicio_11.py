'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, 
às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, 
às coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima "longe" na saída. 
Caso o contrário, quando a distância for menor que 10, imprima "perto"
'''

import math

# Leitura das coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Cálculo da distância entre os dois pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verificação da distância e impressão da resposta
if distancia >= 10:
    print("longe")
else:
    print("perto")