#Escreva um programa que leia a velocidade do carro.
#Se ele estiver acima de 80km/h, mostre uma mensagem que ele foi multado
#  A multa vai custar R$7 por cada KM acima do limite

#Cores
corverde ='\033[32m'
corpadrao ='\033[0;0m'
coramarelo = '\033[33m'
cormagenta = '\033[35m'
corazul = '\033[34m'
corvermelha = '\033[31m'
negrito = '\033[1m'

v = int(input(corpadrao+'Digite a velocidade do seu carro: '))
m = (v - 80) * 7
if v > 80:
    print(corvermelha+'Você foi', negrito+' MULTADO ', 
          corpadrao +corvermelha+'por ultrapassar o limite permitido de 80Km/h, a multado ficou em:',
          coramarelo+ negrito + f'R${m}'+corpadrao)
else:
    print(corverde+'Você esta dirigindo muito bem!'+corpadrao)