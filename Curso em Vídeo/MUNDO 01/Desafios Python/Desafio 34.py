# Calcule o aumento do salário dos funcionários.
# superior a R$1.250, aumento de 10%
# inferior aumento de 15%
s = float(input('Digite o salário do funcionário: R$'))
if s >= 1250:
    novo = (s * 0.10) + s
else:
    novo = (s * 0.15) + s
print('Seu novo salário é de: R${}'.format(novo))
