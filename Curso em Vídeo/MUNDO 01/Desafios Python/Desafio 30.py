# Crie um programa que leia um número inteiro e mostre na se ele é PAR ou IMPAR
# Escreva um programa que leia a velocidade do carro.
# Se ele estiver acima de 80km/h, mostre uma mensagem que ele foi multado
#  A multa vai custar R$7 por cada KM acima do limite

# variaves de cor
corverde = '\033[32m'
corpadrao = '\033[0;0m'
coramarelo = '\033[33m'
cormagenta = '\033[35m'
corazul = '\033[34m'
corvermelha = '\033[31m'
negrito = '\033[1m'

i = int(input('Digite um número: '))
x = i % 2
if x == 0:
    print('O número digitado é', corazul + negrito +' PAR' + corpadrao)
else:
    print('O número digitado é', negrito + cormagenta + ' ÍMPAR'+corpadrao)
