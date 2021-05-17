"""
O bloco Try Except

Utilizamos o bloco para tratar erros que podem ocorrer no nosso codigo prevenindo assim que o programa pare de funcionar
e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:
try:
    //Execução problematica
except:
    //Oque deve ser feito em caso de problema

OBS: Tratar problemas de forma generica nao é am lehor forma. O ideal é sempre tratar de forma especifica
como o raise faz
"""

# Exemplo -Apresentnado erro generico
try:
    geek()
except:
    print('Houve um problema')

# Exemplo tratando erro especifico
try:
    geek()
except NameError: # Precisa ser do tipo certo, porque se colocar NameError e nao sendo um NameError nao adianta
    print('Voce esta utilizando uma função inexistente')
print('')
try:
    len(5)
except TypeError as err: # Com detalhes do erro, bom para salvar em logs
    print(f'A aplicação retornou o seguinte erro: {err}')
print('')
try:
    len(5)
except TypeError as erra:
    print(f'Deu TypeError: {erra}')
except NameError as erra:
    print(f'Deu NameError: {erra}')
except:
    print('Deu um erro diferente')


def pegavalor(dicionario, chave):
    try:
        return dicionario[chave]
    except:
        return None

print('')
dic = {'nome': 'geek'}
print(pegavalor(dic, 'nome'))
print(pegavalor(dic, 'Game'))
print(pegavalor(dic, 8))
