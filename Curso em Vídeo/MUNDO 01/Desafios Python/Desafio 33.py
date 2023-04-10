#Faça um programa que leita três números e mostre qual é o maior e qual é o menor
x = float(input('Digite um número: '))
y = float(input('Digite outro número: '))
i = float(input('Digite um terceiro número: '))
n = [x,y,i]
print('O maior número dentre os três é: {}'.format(max(n)))
print('O menor número dentre os três é: {}'.format(min(n)))