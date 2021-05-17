"""
Listas Aninhadas
- Algumas linguagens de programaçao (C, Java, PHP...) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Araays ou vetores)
    - Multidimensionais (Matrizes)

Em python nós temos as listas
Lista = [1, 'b', 3, 4.22, True] # Podem ser qualquer tipo de dado

"""

# Exemplos
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
print(lista)
print(type(lista))
print('')
# Como acessar os dados
print(lista[0])
print(lista[0][2])
print(lista[2][1])
print('')

# Iterando com loops em uma lista aninhada
for listas in lista:
    for numero in listas:
        print(numero)
print('')
# List Comprehension
[[print(valor) for valor in listas] for listas in lista]

# Gerando tabuleiro/Matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
