#Forma que pesquisei
i=int(input(' Hora da tabuada\n Digite um número: '))
print('='*15)
print(f'Tabuada do {i}')
print('='*15)
for x in range(1,11):{
    print(f'{i} x {x} = {i*x}')
    }
print('='*15)