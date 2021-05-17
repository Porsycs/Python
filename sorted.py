"""
Sorted
Não confunda apesar do nome com a função sort que ja estudamos em lista, o sort só funciona em listas
    Podemos usar o sorted em qualquer iteravel.

Como o proprio nome diz ele serve para ordenar os elementos mas cria uma nova lista diferente do sort que apenas altera
"""
lista = [4, 7, 3, 2, 1, 8]
lista.sort()
print(lista)

# Tuple
# tuple(lista.sort())
# print(tuple(lista)) Erro ja que sort é para lista

print(tuple(sorted((lista)))) # Sorted sempre retorna uma lista com os elementos ordenados

# Adicionando parametros ao sorted
numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse = True)) # Reverse -> Do maior para o menor

# Podemos utilizar o sorted para coisas mais complexas

usuarios = [
    {'Username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro pizzas']},
    {'Username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'Username': 'Jeff', 'tweets': []},
    {'Username': 'Bob123', 'tweets': [], 'Cor': 'Amarelo'},
    {'Username': 'Doggo', 'tweets': ['Eu gosto de café', 'Vou sair hoje!']},
    {'Username': 'Gal', 'tweets': [], 'Cor': 'Preto', 'Musica': 'Rock'}
]

print(sorted(usuarios, key=lambda usuario: usuario['Username'])) # Ordenaçao em dict informando a key para ordenar

print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

print("")

musicas = [{'titulo': 'Thundershock', 'Tocou': 3},
           {'titulo': 'Dead Skin Mask', 'Tocou': 2},
           {'titulo': 'Back in black', 'Tocou': 4},
           {'titulo': 'Sweet child o mine', 'Tocou': 32}
]

# Da menos tocada para a mais
print(sorted(musicas, key=lambda musica: musica['Tocou']))

# Da mais tocada para a menos
print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))
