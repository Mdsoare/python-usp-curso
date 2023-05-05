'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escrever um programa que permita jogar o NIM contra o computador de forma ética.
'''
import random

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vez_do_computador = False
    
    if n % (m+1) == 0:
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
        vez_do_computador = True
    
    while n > 0:
        if vez_do_computador:
            jogada_computador = min(n, m)
            n -= jogada_computador
            print(f"\nO computador tirou {jogada_computador} peça(s).")
            vez_do_computador = False
        else:
            jogada = int(input("Quantas peças você vai tirar? "))
            while jogada > m or jogada < 1 or jogada > n:
                print("Oops! Jogada inválida! Tente de novo.")
                jogada = int(input("\nQuantas peças você vai tirar? "))
            n -= jogada
            print(f"\nVocê tirou {jogada} peça(s).")
            vez_do_computador = True
            
        if n > 0:
            print(f"Agora restam {n} peça(s) no tabuleiro.\n")
        else:
            print("Fim do jogo! O computador ganhou!" if vez_do_computador else "Parabéns! Você ganhou!\n")
    
    return not vez_do_computador

def campeonato():
    print("\n**** Rodada 1 ****\n")
    vitorias_computador = 0
    vitorias_jogador = 0
    for i in range(1, 4):
        print(f"**** Rodada {i} ****\n")
        vencedor = partida()
        if vencedor:
            vitorias_jogador += 1
        else:
            vitorias_computador += 1
    
    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {vitorias_jogador} X {vitorias_computador} Computador")

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