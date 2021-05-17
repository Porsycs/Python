"""
Utilizando lambdas
    Conhecidas como expressoes lambda, sao funçoes sem nome, ou seja, anonima

# Função em python
def soma (a, b):
    return a + b

"""
# Função comum


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))
print('')

# Expressao lambda

lambda x: 3 * x +1

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

# Podemos ter expressoes lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Victor', 'Bueno'))

# Outro exemplo
autores = ['Izaac Asimov', 'Ray Bradbury', 'Robert Heinlen', 'Arthur Doyle', 'Frank Herpert', 'Orson Scorr Dard', 'Douglas Adams',
 'H. G. Wells', 'Leigh Brackett']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # Arrumando em ordem alfabetica do sobrenome
print(autores)
print('')

# Função Quadratica
# f(x) = a * x ** 2 + b * x + c


def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
print(funcao_quadratica(2, 3, -5)(1)) # Ja sai direto
