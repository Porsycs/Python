"""
Zip

zip() -> Cria um iteravel chamado zip object que agrega elementos de cada um dos iteraveis passados como entrada em
pares
"""

# Exemplo
lista = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionario

print(list(zip1))

# O zip utiliza como parametro o menor tamanho em iteravel
lista3 =[1, 2, 3, 4, 5, 6, 7, 8]
zip1 = zip(lista,lista2,lista3)
print(list(zip1)) # Ignorou os outros valores da lista 3

# Lista de tuplas
dados = (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)
print(list(zip(*dados)))

# Exemplo
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)} # Maior valor entre duas notas
print(final)

# Podemos usar map para isso
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
