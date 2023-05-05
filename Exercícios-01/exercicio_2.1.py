'''
Data: 04/05/2023
Autor: Marcelo Soares
Descrição: Exercício proposto para receber quatro notas, calcular e imprima a média aritmética. 
'''
# Recebe quatro notas digitadas pelo usuário, verificando se são valores numéricos válidos:
try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota:"))
    
    if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10 and 0 <= n4 <= 10):
        print("Erro: As notas devem estar entre 0 e 10!")
    else:
        # Calcula a média aritmética das quatro notas:
        rst = (n1 + n2 + n3 + n4) / 4
        # Exibe o resultado na tela:
        print(f"A média aritmética das notas é {rst:.2f}.")
except ValueError:
    print("Erro: Todas as notas devem ser números decimais!") 