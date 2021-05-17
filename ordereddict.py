"""
Module Collections - Ordered Dict

É um dicionário que garante a ordem de inserção dos elementos
"""

from collections import OrderedDict
#Em um dicionario a ordem de inserçao de elementos não é garantida

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 4, 'e': 5})
for chave,valor in dicionario.items():
    print(f'Chave: {chave} Valor: {valor}')
print('')
# Entendendo a diferença de dicionario e Ordered

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2) # A ordem não importa já que são os mesmos elementos

#OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2) # Nesse caso a ordem dos elementos importa então retorna False