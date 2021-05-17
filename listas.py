"""
Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinâmicos e tambem de podermos por QUALQUER tipo de dado.

Linguagens C/Java:
    Arrays possuem tamanho e tipo de dado fixo;
    Ou seja nessas linguagens se criar um array de tipo int e com tamanho 5, este array sera SEMPRE do tipo inteiro
    e poderá ter sempre no máximo 5 valores.

Já em python:
    - Dinâmico: Não possui tamanho fixo; Ou seja podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: As listas não possuem tipo de dado fixo;Ou seja podemos colocar qualquer tipo de dado;

As listas em python ficam em cochetes: []

"""

type([])


lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University') # O mesmo que a lista 2 mas mais simples

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

#Podemos facilmente checar se determinado valor esta contido na lista

num = 7

if num in lista4:
    print('')
    print(f'Encontrei o número {num}')

else:
    print('')
    print(f'Não encontrei o numero {num}')

if 'e' in lista5:
    print('Encontrei a letra E')

else:
    print('Não encontrei a letra E')

#Podemos ordenar uma lista

lista1.sort()
print(lista1) #Lista ordenada

lista2.sort()
print(lista2) #Em string espaço primeiro depois maiusculas em ordem alfabetica e minusculas

#Podemos contar o numero de ocorrências de um valor em uma lista

print(lista1.count(1)) #Conta quantos números 1 tem na lista
print(lista2.count('e'))

"""
Para adicionar elementos em lista usamos a função append (Acrescentar)

OBS: Com append nós só conseguimos adicionar um elemento por vez
"""

print(lista1)
lista1.append(42) #Adiciona o elemento 42 no fim do array
print(lista1)

#Erro só pode um argumento: lista1.append(12, 35, 56)
lista1.append([8, 3, 1])
print(lista1)

if [8, 3 ,1] in lista1:
    print('')
    print('Encontrei a lista!')

else:
    print('')
    print('Não encontrei a lista!')

if [22, 27, 27] in lista1:
    print('')
    print('Encontrei na lista!')

else:
    print('')
    print('Não encontrei na lista!')

lista1.extend([123, 44, 67]) #Adicionando mais números na lista não podendo ser só um valor nesse caso usa append
print(lista1)

#Podemos inserir um novo elemento na lista informando a posição do índice
lista6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista6.insert(2,'Novo valor') # Inserindo um valor mas não substituindo
print(lista6)

#Juntar duas listas

#lista7 = lista1 + lista2
#print(lista7) Ou

lista1.extend(lista2)
print(lista1)

#Forma 1
lista1.reverse() #Inverter a lista
print(lista1)

#Forma 2
print(lista1[::-1]) #Inverter de outra forma

#Copiar uma lista
lista8 = lista2.copy()
print(lista8)

#Tamanho de uma lista (len de lenght)
print(len(lista1))

#Remover ultimo elemento de uma lista
lista10 = [0,1,2,3,4,5]
lista10.pop()
print(lista10)

#Remover elemento pelo índice
#OBS: Se não houver elemento no índice dado ocorre um erro
lista10.pop(2)
print(lista10)

#Podemos remover todos elementos de uma lista
lista10.clear()
print(lista10)

#Repetir elementos da lista
nova = [1, 2, 3]
nova*=3
print(nova)
print('')
#Converter string em lista
curso = 'Curso de python essencial ao avançado'
print(curso)
curso = curso.split()
print(curso)

#Exemplo 2
curso = 'Programação,em,python,essencial'
curso = curso.split(',') #Dizendo que o separador é a virgula ao invés do espaço
print(curso)

#Juntar uma lista para formar string
curso = ['Programação','Em','Python','Essencial']
novo = ' '.join(curso)
print(novo)
print('')

#Somando listas números
lista11 = [1, 2, 3, 4, 5]
soma = 0
for elemento in lista11:
    print(elemento)
    soma += elemento
print(soma)
print('')
#Somando lista string
lista12 = list('Geek University')
soma = ''
for elemento in lista12:
    print(elemento)
    soma += elemento
print(soma)
print('')

#Para facilitar:
lista = [1, 2, 3, 4, 5]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

