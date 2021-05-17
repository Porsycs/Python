"""
Len, Abs, Sum e Round

len() -> Retorna o numero de itens de um iteravel

Abs() -> Retorna o valor absoluto de um numero inteiro ou real de forma basica seria seu valor real sem o sinal

sum() -> Recebe como parametro um iteraveel podendo receber um valor inicial e retorna a soma total dos elementos, inclu
indo o valor inicial (OBS: o valor inicial default é 0)

round() -> Retorna um numero arrendodado para n digito de precisão apos a casa decimal. Se a precisao nao for informada
retorna o inteiro mais proximo da entrada
"""

print(len('Geek university'))
print(len([1, 2, 3, 4, 5]))

# Quando utilizamos a função len o python faz o seguinte:
print('Geek University'.__len__())
print([1, 2, 3, 4, 5].__len__())
print('')

print(abs(-5))
print(abs(5))
print(abs(-14))
print(abs(-3.14)) # Não existe abs de string
print('')

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum(dict(a=1, b=2, c=3, d=4, e=5).values()))
print('')

print(round(10.2))
print(round(10.5))
print(round(1.21212121212, 2))
print(round(3.1415926, 4))
