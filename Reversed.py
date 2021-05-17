"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas
    A função reverse só funciona em listas, já a função reversed funciona com qualquer iteravel.
    ela inverte o iteravel.

A função reversed retorna um iteravel chamado list_reversediterator
"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista,tupla ou conjunto

print(list(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')
print('')

# Podemos fazer o mesmo sem uso de for
print(''.join(list(reversed('Geek University'))))

# Fazer isso com slice de strings
print('Geek University' [::-1])

# Podemos tambem usar reversed para fazer um loop for reverso

for n in reversed(range(0, 10)):
    print(n)

