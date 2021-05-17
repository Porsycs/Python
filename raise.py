"""
Levantando os proprios erros com raise

raise -> Lança exceçoes

OBS: raise nao é uma funçao, é uma palavra reservada assim como def ou qualquer outra em python
pense no raise como sendo util para nos criarmos nossas proprias exceçoes e mensagens de erros

raise TipoDoErro('Mensagem de Erro')
O raise como o return finaliza a função entao nada depois dele sera considerado
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Não é uma string')
    if type(cor) is not str:
        raise TypeError('Não é uma string')
    if cor not in cores:
        raise ValueError(f'As cores precisam ser uma dessas: {cores}')
    else:
        print(f'O texto: {texto} sera impresso na cor {cor}')


texto = input('Digite um texto: ')
cor = input('Digite a cor do texto: ')
colore(texto, cor)

