# Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o usuário
# Tentar descobrir qual foi o número escolhido pelo computador
# o programa deverá escrever na tela se o usário acertou ou não.

#Bibliotecas
import random
from time import sleep

#Cores
corverde ='\033[32m'
corpadrao ='\033[0;0m'
coramarelo = '\033[33m'
cormagenta = '\033[35m'
corazul = '\033[34m'
corvermelha = '\033[31m'
negrito = '\033[1m'

#Comandos
x = random.randint(0,5)
print(coramarelo +'-=-'*20 + corpadrao)
print(negrito + corazul +'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(coramarelo +'-=-'*20 + corpadrao)
y = int(input(cormagenta+'Vamos ver se você sabe qual número inteiro estou pensando entre 0 e 5 \nDigite um número: '))
print(corazul + negrito + 'PROCESSANDO...' + corpadrao)
sleep(2)
if x == y:
    print(corverde +f'Acertou. Parabéns!!! \n Eu pensei realmente no {x}' + corpadrao)
else:
    print(corvermelha +'Errou, eu pensei no {} e não no {}'.format(x, y) + corpadrao)

