"""
Definindo funções

- Funçoes são pequenos trechos de codigos que realizam tarefas específicas
- Pode ou não receber entradas de dados e retornar resultados
- Podemos utiliza-la sem ter que reescreve-la varias vezes

OBS: Se escrever uma funçao que executa varias tarefas dentro dela, é bom fazer uma verificação para que ela seja
simplificada

Já utilizamos várias funçoes desde que o curso foi iniciado como:
print(),
len(),
max,
min,
count e muitas outras

Em python a forma de definir funçoes é:

def nome_da_função(Parametro de entrada):
    bloco_da_função

Onde nome da função sempre em letra minuscula e caso composto deve se usar underline
Parametros de entrada -  são opcionais, onde tendo mais de um devem ser separados por virgulas
Bloco da função - Onde o processamento acontece, podendo ter ou não retorno na função.

OBS: Veja que para definir função usamos a palavra def, informando que estamos definindo uma funçao
tambem abrimos o bloco de codigo com os dois pontos (:) que é utilizado em python para definir blocos

"""
# Exemplo funçoes
cores = ["Verde", 'Vermelho', 'Amarelo', 'Azul']

# Funçoes intregadas (Padrões do python)
print(cores)

# Definindo primeira função
def diz_oi():
    print('Oi')

diz_oi() # Chamada da função

def cantar_parabens():
    print("Parabens pra voce")
    print("Nessa data querida")
    print("Muitas felicidades")

cantar_parabens()