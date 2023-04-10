# ler três retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input('Quer saber se poder fazer um triângulo com três retas? Simples\nMe irfome a medida das três retas:\n Reta A = '))
b = float(input('Reta B = '))
c = float(input('Reta C = '))
d = [a, b, c]
m = max(d)
t = sum(d) - m
if t <= m:
    print('Essas retas NÃO PODEM FORMAR um triângulo!')
else:
    print('Essas retas PODEM FORMAR um triângulo!')
