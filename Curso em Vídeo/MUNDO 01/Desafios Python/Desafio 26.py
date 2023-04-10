# Digite uma frase qualquer e mostre:
#                  - Quantas vezes aparece a letra 'A'
#                  - Em que posição aparece ela pela primeira vez
#                  - Em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).upper().strip()  
print('A letra (A) aparece {} \nA posição que aparece na primeira vez é {} \n A última posição que ela aparece é {}'
      .format(frase.count('A'),frase.find('A') + 1, frase.rfind('A') + 1))
