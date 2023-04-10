from random import sample
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
l = [a1, a2, a3, a4]
print('A sequência é {}' .format(sample(l,k=4)))