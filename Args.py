"""
Entendendo o *args

- O *args é um parametro como outro qualquer, isso significa que podera chama-lo de qualquer coisa desde
 que comece com *. mas por convenção chamamos de *args

 Mas porque *args
    O parametro args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.Então desde
    ja lembre-se de que tuplas sãpo imutaveis
"""

# Exemplos


def soma_todos_numeros(a=1, b=2, c=3):
    return a + b + c


print(soma_todos_numeros(4, 6, 9))

# Entendend args


def soma_todos(*args):
    return sum(args)


print(soma_todos())
print(soma_todos(1))
print(soma_todos(1, 2))
print(soma_todos(1, 2, 3))
print(soma_todos(1, 2, 3, 4))
print('')


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    else:
        return'Eu não sei quem você é'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.1415))
print('')


def soma_lista(*args):
    return sum(args)


lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(soma_lista(*lista)) # Transformando a lista em uma tupla para usar o args