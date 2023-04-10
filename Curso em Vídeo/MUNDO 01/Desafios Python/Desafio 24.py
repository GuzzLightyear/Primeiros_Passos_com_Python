# Ler um nome da cidade e ver se ela começa ou não com o nome
# 'SANTO'
name = str(input('Digite seu nome completo ')).strip()
print('Seu nome começa com Santos? {}'
      .format('Sim' if name[:5].lower() == 'santo' else 'Não'))
