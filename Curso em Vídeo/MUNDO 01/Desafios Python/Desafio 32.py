# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto
from datetime import date
y = int(input('Que ano quer analisar? Digite 0 para ver o ano atual: '))
if y == 0:
    y = date.today().year
print(f'O Ano {y} é Bissexto' if y % 4 == 0 and y %
      100 != 0 or y % 400 == 0 else f'O Ano {y} não é Bissexto')
