"""
Módulo Collections - Counter (Contador)

Collections => High-Performance Container DateTypes

Counter => Recebe um interável como parametro e cria um objeto do tipo Collections counter
que é parecido com o dicionario,contendo como chave um elemento da lista que passamos como parametro e como valor a
quantidade de ocorrencias desse elemento.
"""

# Utilizando o Counter

from collections import Counter

# Podemos usar qualquer iterável, aqui usamos uma lista
# Exemplo 1
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

res = Counter(lista)
print(type(res))
print(res)
print('')

# Veja que para cada elemento da lista ele criou uma chave e mostrou a quantidade de ocorrencias

# Exemplo 2
print(Counter('Geek University'))

# Exemplo 3
texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob
o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável, que todos possam editar
e melhorar. O projeto é definido pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative Commons
BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — desde que respeitando os termos
e condições de uso.
Todos os editores da Wikipédia são voluntários. Eles integram uma comunidade colaborativa, sem um líder, na qual os membros
coordenam os seus esforços no âmbito dos projetos temáticos e diversos espaços de discussão. Dentre as várias páginas de
ajuda à disposição dos interessados em contribuir, estão as que explicam como criar um artigo ou editar um artigo. Em caso
de dúvidas, não hesite em perguntar."""
palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)
print(res.most_common(5)) # As 5 palavras com mais ocorrências no texto

