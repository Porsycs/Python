"""
Funçoes com parametros ( de entrada )

- Funçoes que recebe mdados para serem processados dentro das mesmas
    Se pensarmos em programa qualquer, geralmente temos:
entrada -> processamento -> saida

    Se pensarmos em uma função, ja sabemos que temos funçoes que:
- Nao possuem entrada
- Não possuem saida
- Possuem entrada mas nao saida
- Não possuem entrada mas possuem saida
- Possuem entrada e saida
"""

# Refatorando a função


def quadrado(numero):
    return numero ** 2
    # return numero * numero


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))


def cantar_parabens(nome):
    print('Parabens pra voce nessa data querida'
          ' muitas felicidade '
          'muitos anos de vida'
          f' Parabens {nome}!')


print(cantar_parabens('Victor'))


# Funçoes podem ter n parametros de entrada ou seja podemos colocar quantos parametros forem necessarios.


def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


print(soma(2, 3))
print(multiplica(50, 100))
