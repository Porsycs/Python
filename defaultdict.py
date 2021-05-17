"""
Default dict - Módulo Collections

Ao criar um dicionario utilizando-o nos informamos o valor default, podendo utilizar
um lambda para isso. Esse valor será utilizado sempre que não houver um valo definido
Caso tentemos acessar uma chave que não existe, o valor default é retornado.

OBS: Lambda são funçoes sem nome que podem ou não receber parametros de entrada e retornar valores
"""
from collections import defaultdict

dicionario = {'Curso':'Programação em python'}
print(dicionario)
print(dicionario['Curso'])
#print(dicionario['outro']) Da erro por nã oexistir o 'outro'
print('')

dicionario = defaultdict(lambda: 0)
dicionario['Curso'] = 'Programação python essencial'
print(dicionario['Curso'])
print(dicionario['Outro'])
