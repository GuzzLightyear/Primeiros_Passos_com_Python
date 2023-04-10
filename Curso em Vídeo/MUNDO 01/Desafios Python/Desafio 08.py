i = float(input('Tamanho em Metros = '))
print('O valor em Metros é {}M \n Em centímentros fica {:.0f}cm \n Em milímetros {:.0f}mm'
      .format(i, (i*pow(10,2), i*pow(10,3))))