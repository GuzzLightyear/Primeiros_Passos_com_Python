# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 para viagens mais longas
d = int(input('Digite a distância que deseja viajar em Km: '))
if d <= 200:
    preço = d * 0.5
else:
    preço = d * 0.45

print('O valor da sua passagem vai sair por R${:.2f}'.format(preço))
