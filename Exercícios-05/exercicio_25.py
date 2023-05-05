'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Refaça o exercício anterior imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
'''

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    for j in range(largura):
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()