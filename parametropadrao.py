"""
Funçoes com parametro padrao

- Funçoes onde passagem de parametro seja opcional

Usamos parametros default para evitar erros e flexibilidade ja que evita erro ao esquecer de passar os parametros
"""

print('Geek University')

print()

# Parametro obrigatorio
def quadrado(numero):
    return numero ** 2


def exponencial(numero=10, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))
print(exponencial()) # Parametro opcional, ja que na função tem numeros padrao.


def mostra_info(nome = 'Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return'Pensei que voce fosse o instrutor'
    else:
        return f'Ola {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('Ozzy'))
