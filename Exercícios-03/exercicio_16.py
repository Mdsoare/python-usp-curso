'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
'''
while True:
    try:
        num = int(input("Digite um número inteiro positivo: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros positivos.")

if num <= 1:
    print("não primo")
else:
    eh_primo = True

    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("primo")
    else:
        print("não primo")