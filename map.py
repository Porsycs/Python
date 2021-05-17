"""
Map
    - Com map. fazemos mapeamento de valores para funçao.
"""
import math

def area(raio):
    """Calcula a area de um circulo"""
    return math.pi * (raio ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for raio in raios:
    areas.append((area(raio)))

print(areas)

# Forma 2 Map
areas = map(lambda raio: math.pi * (raio ** 2), raios)
# Ou areas = map(area, raios)
print(list(areas)) # List ,Tuple, Set... Tanto faz
print('')

# Mais um Exemplo
cidades = [('Berlin', 29), ('Cairo', 36), ('Bueno Aires', 19), ('Los Angeles', 26), ('Tokyo', 27)]
print(cidades)
Celsius_Para_Fahrenheit = lambda dado: (dado[0], round(9/5 * dado[1] + 32))
print(list(map(Celsius_Para_Fahrenheit, cidades)))
