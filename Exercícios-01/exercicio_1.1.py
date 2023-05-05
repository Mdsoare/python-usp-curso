'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para calculo de perímetro e área de um quadrado
'''
# Recebe valor digitado pelo usuário fazendo um "cast" de string para int:
try:
    lado = int(input("Digite o valor correspondente ao lado de um quadrado: "))
    if lado <= 0:
        print("O valor digitado deve ser um número positivo!")
    else:
        perimetro = lado * 4
        area = lado ** 2
        print(f"Para um quadrado de lado {lado}:")
        print(f"O perímetro é {perimetro} e a área é {area}.")
except ValueError:
    print("Erro: Você deve digitar um número inteiro para o lado do quadrado!")