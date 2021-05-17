"""
Debugando erros com PDB

PDB - Python debugger


"""
#OBS: A utilização do print para debugar código é uma pratica ruim
def dividir(a, b):
    print(a, b)
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

#Existem formas mais profissionais de se fazer esse debug utilizando o debugger
#Em python podemos fazer isso em diferentes IDEs como o pycharm ou utilizando o PDB

#Pycharm


def dividir1(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir1(4, 7))