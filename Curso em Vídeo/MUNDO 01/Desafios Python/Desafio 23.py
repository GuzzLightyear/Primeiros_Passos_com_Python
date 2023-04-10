# Ler um número de 0 a 9999 e mostre na tela
# os digitos separados.
# ex: 1834 unidade: 4; dezena: 3; centena: 8; milhar: 1

i = int(input('Digite um número de 0 até 9999: '))
u = i // 1 % 10
d = i // 10 % 10
c = i // 100 % 10
m = i // 1000 % 10
print("""
===========
Unidade:{}
Dezena: {}
Centena:{}
Milhar: {}   
===========
      """.format(u, d, c, m))
