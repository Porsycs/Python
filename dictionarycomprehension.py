"""
Dictionary Comprehension

Pense no seguinte:

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4) ou 1, 2, 3, 4

set = {1, 2, 3, 4}

dicionario = {'a': 1, 'b': 2, 'c': 3}

# Sintaxe
    {chave:valor for valor in iteravel}
"""

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numero = [1, 2, 3, 4]
quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos com logica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 ==0 else 'impar') for num in numeros}
print(res)