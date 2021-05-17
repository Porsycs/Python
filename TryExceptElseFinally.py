"""
Try / Excepct / Else / Finally

Dica de quando e onde tratar codigo:
        - TODA ENTRADA DE DADO DE USUARIO DEVE SER TRATADA!

Else só é executado se não acontecer o erro
Else e Finally não são tão usados
Finally é executado tendo erro ou não geralmente utilizado para fechar ou desalocar recursos

O tratamento para ser organizado e efetivo deve ser feito dentro das funçoes como no ultimo exemplo

"""

try:
    num = int(input('Informe um numero: '))
except ValueError: # Caso erro imprimir esse
    print('Entrada de valor incorreta!')
else: # Se nao ocorrer erro imprimir esse
    print(f'Voce digitou: {num}')
print('')

try:
    num = int(input('Informe um numero:'))
except ValueError:
    print('Valor invalido')
else:
    print(f'Voce digitou o numero: {num}')
finally:
    print('Executando finally')

# OBS: O bloco finally é sempre executado independente se houve exceção ou não
print('')

# Exemplo mais complexo


def dividir(a, b): # Os tratamentos devem ser feitos dentro da função
    try:
        return int(a) / int(b)
    except ValueError: # Forma mais complexa, o generico seria apenas o except que trataria de todos!
        return'Valor inválido'
    except ZeroDivisionError:
        return'Não é possivel dividir por 0!'


num1 = input('Informe o primeiro numero:')
num2 = input('Informe o segundo numero:')
print(dividir(num1, num2))
print('')

# Semi-Genérico


def dividir(a, b): # Os tratamentos devem ser feitos dentro da função
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err: # Forma Semi-Generica
        return f'Valor inválido {err}'


num1 = input('Informe o primeiro numero:')
num2 = input('Informe o segundo numero:')
print(dividir(num1, num2))

