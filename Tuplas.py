"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas. Existem duas diferenças básicas:
1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela nunca se muda. Toda operação em uma tupla gera
uma nova tupla.

Porque usar tuplas?
- Tuplas são mais rápidas que listas.
- Deixa o codigo mais seguro já que são imutáveis.

"""

#CUIDADO: As tuplas são representadas por parenteses mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
#Ambas são tuplas
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  #Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) #Isso é uma tupla
print(tupla4)
print(type(tupla4))

#CONCLUSÃO: Tuplas são definidas pelo uso de virgula e não pelo parenteses

#Podemos gerar uma tupla dinamicamente com range:

tupla = tuple(range(11))
print(tupla)

#Desempacotamento de tupla:

tupla5 = ('Geek University', 'Programação em Python')
escola, curso = tupla5
print(curso)
print(escola)

#Métodos para adição e remoção de elementos na tupla não existem por serem imutáveis.

#Soma*, Valor maximo*, Valor minimo* e Tamanho (* Somente se os valores forem reais).
tupla6 = (1, 2, 3, 4, 5, 6)
print(sum(tupla6))
print(max(tupla6))
print(min(tupla6))
print(len(tupla6))

#Concatenação de tuplas

tupla7 = (1, 2, 3)
tupla8 = (4, 5, 6)
print(tupla7+tupla8) #Se juntam mas não se alteram. Para alterar: tupla9 = tupla7 + tupla8
#Ou tupla7 +=tupla8

#Verificar se determinado elemento esta na tupla:

tupla10 = (1, 2, 3)
print(3 in tupla10)
print(33 in tupla10)

for n in tupla10:
    print(n)

for indice, valor in enumerate(tupla10):
    print(f'[{indice}]', valor)

#Contando elementos da tupla:

tupla11 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla11.count('a'))

#Devemos usar tuplas sempre que não precisarmos mudar os dados
#Exemplo: Meses

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
#Não faz sentido a lista de meses ser modifica-la

#O acesso a elementos é semelhante a lista
print(meses[5])
print('')
#Iterar com while:
i = 0
while i < len(meses):
    print(meses[i])
    i+=1

#Verificar em qual indice o elemento esta na tupla:

print(meses.index('Dezembro'))

#OBS: Caso não tenho o o indice na lista, retorna erro.

#Slicing:

print(meses[0:])
print(meses[5:9]) # Do 5 até o 9