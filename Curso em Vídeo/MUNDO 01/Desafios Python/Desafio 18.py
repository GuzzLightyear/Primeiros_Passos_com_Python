# Exercício Python 18: Faça um programa que 
# leia um ângulo qualquer e mostre na tela o valor do 
# seno, cosseno e tangente desse ângulo.
from math import cos, tan, sin, radians 
i = float(input('Vamos descobrir o seno cos e tan de um número\n Primeiro digite qualquer ângulo: '))
ir = radians(i)
print('O Seno, COSSENO e a Tangente de {} é \n O SENO é {:.2f} \n O COSSENO é {:.2f} \n A TANGENTE é {:.2f} '
      .format(i, sin(ir), cos(ir), tan(ir)))