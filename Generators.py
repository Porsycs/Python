"""
Generators

Em aulas anteriores nos estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension
    Mas nao vimos tuple Comprehension e porque elas se chamam generators

nomes = ['Carlos','Camila','Cassiano','Cristina']

print(any([nome[0] == 'C' for nome in nomes]))
 - Poderia ser feito usando generators
"""
from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

res2 = (nome[0] == 'C' for nome in nomes)
print(type(res2))

# Generator é mais performatico que list

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92323324144))
print(getsizeof(True))
print('')

# Gerando uma lista com list Comprehension
list_comp = getsizeof([x*10 for x in range(1000)])

# Set comprehension
set_comp = getsizeof({x*10 for x in range(1000)})

# Dict Comprehension
dic_comp = getsizeof({x: x*10 for x in range(1000)})

# Gerando com generators
gen = getsizeof(x * 10 for x in range(1000))

print("Para fazer a mesma tarefa teremos uso de memorias diferentes para a mesma tarefa:")
print(f'Lista: {list_comp}')
print(f'Set: {set_comp}')
print(f'Dictionary: {dic_comp}')
print(f'Generator: {gen}')
