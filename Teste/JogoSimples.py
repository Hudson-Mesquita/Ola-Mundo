# Jogo simples de pedra/papel/tesoura sem interface gráfica
from multiprocessing.connection import wait
from random import choice
from time import sleep
print("-=-" * 15)
print(" " * 9, "\033[1;31mPedra Papel Tesoura V0.3\033[m")
print("-=-" * 15)
print("\nBem vindo(a) ao jogo Pedra Papel Tesoura. \nSerão 5 rounds e quem tiver a maior pontuação final, Ganha!!")
print("-" * 40)
lista = ["Pedra", "Papel", "Tesoura"]
cont = 1
gan = 0
per = 0
while cont <=5:
    print("\nEscolha o número na lista para uma das opções:")
    print("[ 1 ] para escolher \033[34mPEDRA\033[m\n[ 2 ] para escolher \033[33mPAPEL\033[m\n[ 3 ] para escolher \033[31mTESOURA\033[m")
    jogador = int(input("Sua Escolha: "))
    print("\033[34mPedra..\033[m")
    sleep(1)
    print("\033[33mPapel...\033[m")
    sleep(1)
    print("\033[31mTESOURA!!!!\033[m")
    ia = choice(lista)
    if jogador == 1:
        jognome = "Pedra"
    elif jogador == 2:
        jognome = "Papel"
    elif jogador == 3:
        jognome = "Tesoura"
    else:
        print("Número inválido")
        break
    if ia == 'Pedra' and jogador == 2 or ia == 'Papel' and jogador == 3 or ia == 'Tesoura' and jogador == 1:
        print(f"Computador escolheu \033[31m{ia}\033[m e Jogador escolheu \033[34m{jognome}\033[m")
        print(f"\033[32mPARABÉNS!!! Você ganhou o {cont}° Round\033[m")
        gan = gan + 1
    elif ia == jognome:
        print(f"Computador escolheu \033[31m{ia}\033[m] e Jogador escolheu \033[34m{jognome}\033[m, \033[32mEMPATE!!!\033[m")
        print("Haverá um round extra por não ser permissivo empates")
        cont = cont - 1
    else:
        print(f"Computador escolheu \033[31m{ia}\033[m e Jogador escolheu \033[31m{jognome}\033[m")
        print(f"Que pena, \033[31mVocê perdeu o {cont}° Round\033[m")
        per = per + 1
    cont = cont + 1
    if cont < 5:
        print("Vamos para o próximo Round!")
        print("=" * 40)
print(f"Você ganhou {gan} partidas e o Computador ganhou {per} partidas")
if gan > per:
    print("\033[34mVITÓRIA!!!!\033[m")
else:
    print("\033[31mDERROTA\033[m")
print("Obrigado por jogar.")
