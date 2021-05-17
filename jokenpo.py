from random import randint
from time import sleep

x = 1
Empate = 0
Jogador = 0
Computador = 0
while x == 1:
    itens = ['Pedra', 'Papel', 'Tesoura', ]
    computador = randint(0, 2)
    print('Suas opções:\n[0] Pedra \n[1] Papel \n[2] Tesoura ')
    jogador = int(input('Qual sua jogada?'))
    print('JO')
    sleep(0.75)
    print('KEN')
    sleep(0.75)
    print('PO')
    sleep(0.75)
    print('-='*15)
    print('Computador jogou: {}'.format(itens[computador]))
    print('Jogador jogou: {}'.format(itens[jogador]))
    print('-='*15)

    if computador == 0: # Pedra
        if jogador == 0:
            print('Empate')
            Empate += 1
        elif jogador == 1:
            print('Venceu!')
            Jogador += 1
        elif jogador == 2:
            print('Perdeu!')
            Computador += 1
    if computador == 1: # Papel
        if jogador == 0:
            print('Perdeu!')
            Computador += 1
        elif jogador == 1:
            print('Empate!')
            Empate += 1
        elif jogador == 2:
            print('Venceu!')
            Jogador += 1
    if computador == 2: # Tesoura
        if jogador == 0:
            print('Venceu!')
            Jogador += 1
        elif jogador == 1:
            print('Perdeu!')
            Computador += 1
        elif jogador == 2:
            print('Empate!')
            Empate += 1
    x = int(input("Deseja joga novamente?\n1 - Sim\n2 - Não\nResposta: "))
    
print(f'Vitorias: {Jogador} Derrotas: {Computador} Empate: {Empate}')
