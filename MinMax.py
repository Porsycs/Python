"""
Min e Max

max() -> Retorna o maior valor em um iteravel ou o maior de dois ou mais elementos

min() -> Retorna o maior valor em um iteravel ou o menor de dois ou mais elementos
"""

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # Seja de lista tupla set dicionario...

tupla = 1, 8, 4, 99, 34, 129
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = dict(a=1, b=8, c=4, d=99, e=34, f=129)
print(max(dicionario)) # Maior pela chave
print(max(dicionario.values())) # Maior por valor
print('')
# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(f'Maior valor é: {max(val1, val2)}')
print('')

print(max('Geek University')) # Maior letra do alfabeto

# Minimo

lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) # Seja de lista tupla set dicionario...

tupla = 1, 8, 4, 99, 34, 129
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = dict(a=1, b=8, c=4, d=99, e=34, f=129)
print(min(dicionario)) # Maior pela chave
print(min(dicionario.values())) # Maior por valor
print('')
# Faça um programa que receba dois valores do usuario e mostre o menor
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(f'Menor valor é: {min(val1, val2)}')
print('')

print(f'Menor letra: {min("Geek University")}') # Menor letra nesse caso o espaço que conta uma letra.
print('')

nomes = 'Aria', 'Tim', 'Samson', 'Dora', 'Ollivander'

print(max(nomes)) # Ordem alfabetica
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome))) # Maior nome
print(min(nomes, key=lambda nome: len(nome))) # Menor nome
print('')

musicas = [{'titulo': 'Thundershock', 'Tocou': 3},
           {'titulo': 'Dead Skin Mask', 'Tocou': 2},
           {'titulo': 'Back in black', 'Tocou': 4},
           {'titulo': 'Sweet child o mine', 'Tocou': 32}
]

print(max(musicas, key=lambda musica: musica['Tocou']))
print(min(musicas, key=lambda musica: musica['Tocou']))

print(max(musicas, key=lambda musica: musica['Tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['Tocou'])['titulo'])
