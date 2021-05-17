"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


"""
# Biblioteca para trabalhar com dados estatisticos
import statistics

valores = 1, 2, 3, 4, 5, 6
media = (sum(valores)/len(valores))
print(media)

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calcular a media dos dados utilizando a função mean()
media = statistics.mean(dados) # Retorna a media aritmética
print(f'Média: {media}')

# OBS: Assim como a função map a filter recebe dois parametros, sendo uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))
print('')

paises = ['', 'Argentina', 'Chile', 'Brasil', '', 'Colombia', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises) # Vazios são filtrados
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises) # O mesmo que o de cima
print(list(res))
res = filter(lambda pais: pais != '', paises)
print(list(res))

"""
Diferença entre map() e filter()
map() -> Na map recebe dois parametros uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do iteravel
filter()-> Recebe dois parametros uma função e um iteravel e retorna um objeto e filtra retorna um elemento de acordo com a função
"""

# Exemplo mais complexos

usuarios = [
    {'Username': 'Samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro pizzas']},
    {'Username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'Username': 'Jeff', 'tweets': []},
    {'Username': 'Bob123', 'tweets': []},
    {'Username': 'Doggo', 'tweets': ['Eu gosto de café', 'Vou sair hoje!']},
    {'Username': 'Gal', 'tweets': []}
]

# Filtras usuarios inativos

# Forma 1
inativos = filter(lambda user: len(user['tweets']) == 0, usuarios)
print(list(inativos))

# Forma 2
inativos = filter(lambda user: not user['tweets'], usuarios)
print(list(inativos))
print('')

# Combinar filter e map
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo "Sua instrutora é {nomes}" Desde que cada nome tenha menos de 5 caracteres
lista = map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes))
print(list(lista))
