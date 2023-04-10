#=====Raiz Quadrada sem biblioteca=============#
#num = int(input('Digite um número: '))
#print('raiz quadrada {}'.format(num**1/2))
#=====Raiz Quadrada com biblioteca=============#
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #Você precisa colocar a biblioteca para puxar as funcionalidades
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))