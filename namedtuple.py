"""
Module Collections - Named tuple

São tuplas diferenciadas onde especificamos um nome para a mesma e tambem parametros
"""
from collections import namedtuple
tupla = 1, 2, 3
#print(tupla[1])

# Precisamos definir um nome e parametros

# Forma 1
cachorro = namedtuple('Cachorro', 'Idade Raca Nome')

# Forma 2
cachorro = namedtuple('Cachorro', 'Idade, Raca, Nome')

# Usando
ray = cachorro(Idade=3, Raca='Chow-Chow', Nome='Ray')
print(ray)
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2
print(ray.Idade)
print(ray.Raca)
print(ray.Nome)