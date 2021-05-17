"""
- Conjuntos em linguagem de programação nos referimos á teoria dos conjuntos da matematica.

- Aqui no python os conjuntos são chamados de Sets.

Dito isso, na mesma forma como na matematica, Sets ou conjuntos:
    - Não possuem valores duplicados
    - Não possuem valores ordenados
    - Elementos não são acessados via indice

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos
com ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos são criados com chaves ( {} )

Diferença entre Conjunto e mapa(Dicionarios)
    - Um dicionário tem chave/valor
    - Conjunto apenas valor
"""

# Definindo conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})
print(type(s))
print(s) # Note que valores repitidos não são impressos
print('')
# Forma 2 (Mais comum)
s = {1, 2, 3, 4, 5}
print(type(s))
print(s)
print('')

# Assim como todo outro conjunto python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(type(s))
print(s)
print('')

# Usos interessantes com set
cidades = ['Belo horizonte', 'São Paulo', 'Campo grande', 'Cuiaba', 'Campo grande', 'São paulo', 'Cuiaba']
print(cidades)
print(len(cidades)) # Usando lista podemos ver quantas pessoas usando o len

# Com set podemos saber as pessoas das cidades distintas
print(len(set(cidades))) # Assim podemos ver quantas cidades diferentes tem
print('')

# Adicionando elementos
s = {1, 2, 3, 4}
s.add(4)
s.add(5)
print(s)

# Remover dados

# Forma 1
s.remove(5) # Não é o indice, mas sim o valor. Se o valor não existir da erro
print(s)

# Forma 2
s.discard(2) # Não da erro se o valor não existir
print(s)
print('')
# Copiando um conjunto para outro

# Forma 1 Deep Copy
s = {1, 2, 3}
novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)
print('')

# Podemos remover todos elementos
s.clear()
print(s)
print('')

# Imagine dois conjuntos um de estudantes Python e outro Java
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'} # Notamos que algumas pessoas fazem mais de um curso
# Precisamos gerar um conjunto com nome de estudantes únicos

# Forma 1 Usando Union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma 2 Caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar nome dos que estão em ambos cursos

# Forma 1 utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 Usando E comercial &
ambos2 = estudantes_python & estudantes_java
print(ambos2)
print('')

# Gerar conjunto dos que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
print('')
so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma, Valor Max, Valor Mín, Tamanho (Mesmo dos outros)