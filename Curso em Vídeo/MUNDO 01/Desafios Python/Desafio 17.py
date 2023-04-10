#Faça um programa que leia o comprimento do 
#cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
# ============================================================

# from math import pow, sqrt
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto ajacente:' ))
# h = sqrt (pow(co, 2) + pow(ca, 2))
# print('{:.2f}'.format(h))

#######################################################
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto ajacente:' ))
h = hypot(co, ca)
print('{:.2f}'.format(h))