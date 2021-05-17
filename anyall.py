"""
Any e All

all() -> retorna true se todos elementos do iteravel forem verdadeiros ou ainda se o iterario estiver vazio
pode ser qualquer iteravel: lista,set,tuple...

any() -> Retorna true se qualquer elemento do iteravel for verdadeiro, se o iterario estiver vazio retorna False
"""

# Exemplo
print(all([0, 1, 2, 3, 4])) # 1,2,3,4 são True mas 0 é False

print(all([])) # Lista vazia -> True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes])) # Todos nomes iniciam com C -> True

print(all([num for num in [4, 2, 6, 8, 10] if num % 2 == 0]))

# Any
print(any([0, 1, 2, 3, 4])) # True ja que pelo menos um elemento é True

print(any([0, False, {}, [], ()]))

print(any([nome[0] == 'C' for nome in nomes]))
