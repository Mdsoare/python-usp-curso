'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
'''
while True:
    try:
        num = int(input("Digite um número inteiro: "))
        if num <= 0:
            print("O número deve ser maior que zero. Tente novamente.")
        else:
            num_str = str(num)
            tem_adjacente_igual = False
            for i in range(len(num_str)-1):
                if num_str[i] == num_str[i+1]:
                    tem_adjacente_igual = True
                    break
            if tem_adjacente_igual:
                print("sim")
            else:
                print("não")
            break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")