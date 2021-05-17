"""
OBS: Em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas.

Dicionarios são coleçoes tipo chave/valor

Dicionarios são representados por chaves { }

Sobre Dicionarios:
    -Chave e valor são separados por dois pontos (chave : valor)
    -Podem ser de qualquer tipo de dado
    -Podemos misturar tipos de dados
"""

print(type({}))

#Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}
print(type(paises))
print(paises)

#Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

#Acessando elementos

#Forma 1: Via Chave (Igual Tupla)
print('')
print(paises['br'])
print(paises['py'])
#Caso a chave não exista, retorna um erro

#Forma 2: Acessando via Get(Recomendado)

print(paises.get('br'))
print(paises.get('ru')) #None

#Caso não seja encontrado podemos definir um valor padrão:
print(paises.get('ru', 'Não Encontrado'))
print('')

#Boolean se o valor esta na lista:
print('br' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']
print('')
#Localidades:
localidades = {
    (35.6897, 39.697): 'Escritorio em Tokyo',
    (40.111, 74.0068): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
} #Tuplas como chave de dicionário pois são imutaveis.
print(localidades)
print(type(localidades))

#Adicionar elementos no dicionário:
receita = {'jan': 100, 'fev': 120, 'mar': 300 }
print(receita)

#Forma 1:
receita['abr'] = 350
print(receita)

#Forma 2:
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai':500})
print(receita)

#Atualizando dados em dicionario:
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 600})
print(receita)
print('')
#Conclusão 1: Atualizar dados ou acrescentar é da mesma forma
#Conclusão 2: Em dicionarios não podemos ter chaves repetidas

#Remover elementos:

#Mais comum:
receita1 = {'jan': 100, 'fev': 120, 'mar': 300}
receita1.pop('mar')
print(receita1)

#Forma 2:
del receita1['fev'] #Somente se existir senão da erro
print(receita1)
print('')
print('')
"""
Imagine que tem um carrinho de compras:
    Produto 1:
        -Nome
        -Quantidade
        -Preço
        
    Produto 2:
        -Nome
        -Quantidade
        -Preço
"""
#Podemos usar lista - Sim
carrinho = []
produto1 = ['Playstation 5', 1, 4999.99]
produto2 = ['Jogo', 1, 299.99]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla - Sim
produto1 = ('Playstation5', 1, 4999.99)
produto2 = ('Jogo', 1, 299.99)
carrinho = (produto1, produto2)
print(carrinho)

# 3 - Poderiamos utilizar um dicionario - Sim

carrinho = []
produto1 = {'Nome:': 'Playstation 5', 'Quantidade:': '1', 'Preço:': 4999.99}
produto2 = {'Nome:': 'Jogo', 'Quantidade:': '1', 'Preço:': 299.99}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print('')
#Dessa forma podemos facilmente adicionar ou remover produtos do carrinho e saber suas informaçoes.

#Métodos de dicionarios
d = dict(a=1, b=2, c=3)

#Zerar dados
d.clear()
print(d)

#Copiando dicionario para outro
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(novo)

#Keys e chaves
d = dict(a=1, b=2, c=3)
print(d.keys())

for chave in d.keys():
    print(d[chave])

#Acessando os valores
print(d.values())

for valor in d.values():
    print(valor)

for chave, valor in d.items():
    print(f'Chave = {chave} Valor = {valor}')

print(d.items())

#Soma, Valor Máx, Valor Min, Tamanho
print(sum(d.values()))
print(max(d.values()))
print(min(d.values()))
print(len(d))