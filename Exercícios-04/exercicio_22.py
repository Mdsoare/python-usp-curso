'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Reescreva a função 'maximo' do outro exercício, 
que devolve o maior valor dentre dois inteiros recebidos, 
para que ela passe a receber 3 valores inteiros como parâmetros 
e devolva o maior dentre eles.
'''

def maximo(n1, n2, n3):
    if (n1 < n2 < n3) or (n1 > n2 and n1 < n3):
        print(n3)
    elif (n1 < n2 > n3):
        print(n2)
    else:
        print(n1)

maximo(30, 14, 10)
maximo(0, -1, 1)