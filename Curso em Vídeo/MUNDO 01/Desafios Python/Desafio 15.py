#Exercício Python 15: Escreva um programa que pergunte a
#a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Km rodado com o carro: '))
d = int(input('Quantidade de dias que ele foi alugado: '))
t = (d*60) + (km*0.15)
print(f' O carro andou {km}Km\n Por {d} dias\n o Total a pagar é de R${t}')