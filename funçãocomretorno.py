"""
Funçoes com retorno

OBS: Quando uma função nao retorna nenhum valor, o retorno é None

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

def jogar_moeda():
    # Gera um numero random entre 0 e 1
    valor = random()
    print(f'Valor dado: {valor}')
    if valor > 0.5:
        return "Cara"
    else:
        return "Coroa"

print(jogar_moeda())
print('')
"""
from random import random


def pedra_papel_tesoura():
    valor = random()
    if valor <= 0.33333333:
        return "Pedra"
    elif valor > 0.33333333 <= 0.666666:
        return "Papel"
    else:
        return "Tesoura"


y = 1
Humano = 0
IA = 0
Empate = 1
while y == 1:

    x = input("Digite Pedra Papel ou Tesoura:")

    if pedra_papel_tesoura() == 'Pedra':
        print(pedra_papel_tesoura())
        if x == 'Papel':
            print('Você venceu!')
            Humano += 1
        elif pedra_papel_tesoura() == x:
            print('Empate!')
            Empate += 1
        else:
            print('Voce perdeu!')
            IA += 1

    if pedra_papel_tesoura() == 'Papel':
        print(pedra_papel_tesoura())
        if x == 'Tesoura':
            print('Você venceu!')
            Humano += 1
        elif pedra_papel_tesoura() == x:
            print('Empate!')
            Empate += 1
        else:
            print('Voce perdeu!')
            IA += 1

    if pedra_papel_tesoura() == 'Tesoura':
        print(pedra_papel_tesoura())
        if x == 'Pedra':
            print('Você venceu!')
            Humano += 1
        elif pedra_papel_tesoura() == x:
            print('Empate')
            Empate += 1
        else:
            print('Voce perdeu!')
            IA += 1
    y = int(input('Deseja continuar?\n1 - Sim\n2 - Não\nResposta:'))


print(f'Vitorias: {Humano} Derrotas: {IA} Empate: {Empate}')
