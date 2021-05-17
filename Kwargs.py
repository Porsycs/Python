"""
**Kwargs

Este é só mais um parametro mas diferente do args que coloca os valores extras em uma tupla, o **kwargs exige que usemos
parametros nomeados e os transforma em um dicionario.

"""


def cores_favoritas(**kwargs):
    for pessoa,cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(Marcos='Verde', Fernanda='Azul', Larissa='Rosa') # Dicionario

# Os parametros em args e kwargs não são obrigatorios.

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['Geek'] == 'Python':
        return'Voce recebeu um cumprimento pythonico'
    elif'Geek' in kwargs:
        return f"{kwargs['Geek']} Geek"
    else:
        return'Não tenho certeza quem voce é'


print(cumprimento_especial())
print(cumprimento_especial(Geek='Python'))
print(cumprimento_especial(Geek='Oi'))
print((cumprimento_especial(Geek='Especial')))
print('')

# Desempacotar um dicionario


def nome(**kwargs):
    return f"Meu nome é {kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Victor', 'sobrenome': 'Bueno'}
print(nome(**nomes))
