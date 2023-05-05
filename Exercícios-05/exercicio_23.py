'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escrever um programa que permita a uma "vítima" jogar o NIM contra o computador.
OBS: O computador sempre ganha!
'''

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    elif n % (m+1) == 0:
        return m
    else:
        return n % (m+1)

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            print("\nOops! Jogada inválida! Tente de novo.")
            jogada = 0
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m+1) == 0:
        print("\nVocê começa!")
        vez_do_usuario = True
    else:
        print("\nComputador começa!")
        vez_do_usuario = False

    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            print("\nVocê tirou", jogada, "peça(s).")
            vez_do_usuario = False
        else:
            jogada = computador_escolhe_jogada(n, m)
            print("\nO computador tirou", jogada, "peça(s).")
            vez_do_usuario = True

        n -= jogada

        if n == 0:
            if vez_do_usuario:
                print("\nFim do jogo! O computador ganhou!")
                return 0
            else:
                print("\nFim do jogo! Você ganhou!")
                return 1
        else:
            print("Agora restam", n, "peças no tabuleiro.")

def campeonato():
    print("\n**** Rodada 1 ****\n")
    resultado1 = partida()

    print("\n**** Rodada 2 ****\n")
    resultado2 = partida()

    print("\n**** Rodada 3 ****\n")
    resultado3 = partida()

    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", resultado1 + resultado2 + resultado3, "X", 3 - resultado1 - resultado2 - resultado3, "Computador")

def main():
    while True:
        try:
            print("Bem-vindo ao jogo do NIM! Escolha:\n")
            print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n0 - para sair do jogo\n")
            opcao = int(input())
        except ValueError:
            print("Ops! Digite um número válido.\n")
            continue
            
        if opcao == 0:
            print("Você escolheu sair!\n")
            break
        elif opcao == 1:
            print("Você escolheu uma partida isolada!\n")
            partida()
            break
        elif opcao == 2:
            print("Você escolheu um campeonato!\n")
            campeonato()
            break
        else:
            print("Ops! Opção inválida\n")

if __name__ == "__main__":
    main()