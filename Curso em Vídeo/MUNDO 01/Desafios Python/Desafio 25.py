# Ler o nome da pessoa e dizer se ela tem SILVA no nome
name = str(input('Digite seu nome completo: ')).lower().strip()
print('Seu nome tem Silva? {}'.format('Sim' if 'silva' in name else 'Não'))
