# nome completo da pessoa
# mostre: - nome com todas as Letras Maiúsculas
#         - nome com todas as Letras Minúsculas
#         - quantidade de letras ao todo sem considerar espaços
#         - Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo ')).strip()
separa = nome.split()
print('NOME MAIUSCULO: {} \n nome minúsculo: {} \n A Quantidade de letras no seu nome é: {} \n O seu primeiro nome tem {} letras'
      .format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), len(separa[0])))
