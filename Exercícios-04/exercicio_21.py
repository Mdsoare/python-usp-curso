'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve 
'Fizz' se o número for divisível por 3 e não for divisível por 5;
'Buzz' se o número for divisível por 5 e não for divisível por 3;
'FizzBuzz' se o número for divisível por 3 e por 5;
Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.
'''

def fizzbuzz(numero):
    if (numero % 3 == 0 and numero % 5 != 0):
        print("Fizz")
    elif (numero % 5 == 0 and numero % 3 != 0):
        print("Buzz")
    elif (numero % 3 == 0 and numero % 5 == 0):
        print("FizzBuzz")
    else:
        print(numero)

fizzbuzz(3)  # imprime Fizz
fizzbuzz(5)  # imprime Buzz
fizzbuzz(15) # imprime FizzBuzz
fizzbuzz(8)  # imprime 8