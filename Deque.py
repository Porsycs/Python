"""
Modulo Collection - Deque

Podemos dizer que o Deque é uma lista de alta performance
"""

from collections import deque

# Criando deques
deq = deque('Geek')
print(deq)

# Adicionando elementos no Deque
deq.append('y') # Adiciona elemento no final
print(deq)

deq.appendleft('k') # Adiciona no começo
print(deq)

#Remover elementos
deq.pop() # Remove do fim
print(deq)

deq.popleft() # Remove do começo
print(deq)