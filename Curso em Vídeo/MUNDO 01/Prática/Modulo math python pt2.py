#Uma segunda forma de utilizar alguma funcionalidade da biblioteca no python
#é puxando apenas as funcionalidades que vai utilizar, assim você não precisa
#colocar math.'' antes de qualquer funcionalidade exemplo
#para raiz quadrada na pt1 utilizamos 
# import math
# raiz = math.sqrt(num)
# mas podemos fazer assim para facilitar nosso código futuramente, claro se for poucos itens da 
#biblioteca que você for utilizar, ou não haver nomes iguais, caso tenha você tera que referenciar
#para não haver erro
# exemplo:
from math import sqrt # usei from(de) math import(importar puxar) sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))