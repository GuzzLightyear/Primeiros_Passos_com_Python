# Ler o nome completo da pessoa, e mostrar apenas o primeiro e último ex:
# - Ana Maria de Souza, Primeiro = Ana, último = Souza.
name = str(input('Digite se nome completo: ')).title().split()
print('Seu nome completo é: {} \n Seu Primeiro nome é: {}\n Seu último nome é: {}'
      .format(' '.join(name), name[0], name[-1]))
