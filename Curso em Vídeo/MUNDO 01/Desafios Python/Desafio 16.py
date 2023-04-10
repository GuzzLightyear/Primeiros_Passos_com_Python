#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
i = float(input('Digite um número com decimais: '))
print(f'O número {i} tem a parte inteira {trunc(i)}')