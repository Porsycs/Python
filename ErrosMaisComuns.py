"""
Erros mais comuns no python
OBS: Execptions e Errors são sinonimos na programação

É importante ler e aprender a interpretar as saidas de erro geradas pela execução do código

Os erros mais comuns:
    - Syntaxerror -> Quando encontra erro de syntax, ou seja, escreveu algo que python n considera como parte da
    linguagem

    -NameErro -> Ocorre quando uma variavel ou função nao foi definida

    -TypeError -> Ocorre quando uma função/Operação/Ação é aplicada a um tipo errado

    -IndexError -> Quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um indi
    ce invalido.

    -ValueError -> Quando uma função ou operação built-in recebe um argumento com tipo correto mas valor inapropriado

    -KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe

    -AtributeError -> Ocorre quando uma variavel nao tem um atributo ou função

    -IdentationError -> Ocorre quando nao respeitamos a indentação do python que é de 4 espaços


# Exemplo syntaxerror

def funcao: # Falta o parenteses
    print('Geek University')

None = 1 # Palavra reservada como valor

return # Fora de uma função

# Exemplo NameError

print(geek) # Nao foi definido o valor de geek

geek() # Não foi criada uma função chamada geek

a = 10
if a<10:
   msg = 'É maior que 10!'

print(msg) # a é maior que 10 e nao tem uma definição para esse caso

# Exemplo TypeError

print(len(5))
print('Geek' + []) # String unindo com uma lista

# Exemplo IndexError

lista = ['Geek']
print(lista[1]) # Não existe posição 1 na lista, apenas o [0]

# Exemplos ValueError

print(int('Geek')) # Espera receber um numero para converter para int, não uma palavra

# Exemplos KeyError

dic = {}
print(dic['Geek']) # Não existe chave geek no dicionario vazio

# Exemplos AtributeError

tupla = 11, 2, 31, 4
tupla.sort()
print(tupla) # Não existe sort para tupla, apenas para listas

# Exemplos IdentationError

def nova():
print('geek') # Se espera 4 espaços

for i in range(0,10):
print(i) # Não tem 4 espaços
"""
