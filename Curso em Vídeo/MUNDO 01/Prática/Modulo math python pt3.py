#Uma terceira forma de utilizar alguma funcionalidade da biblioteca no python
#é puxando mais de uma funcionalidade
# exemplo:
from math import sqrt, floor #(floor, arredonda pra baixo)
# usei from(de) math import(importar puxar) sqrt, (virgula para adicionar outra funcionalidade no caso) floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, floor(raiz)))