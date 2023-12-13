#Desafio 053
#Crie um programa que leia uma frase qualquer e diga se ela é um palídromo, descosiderando os espaços.

#def is_palindrome(word)
#    j = len(word)-1
#    result = 0
#    for i in range
#        (len(word)):
#        if word [i] == word[j]:
#            result = result + 1
#        if i >= j:
#            break
#        j = j - 1

        #Até aqui já fizemos a verificação de todos os pares de letras na lógica do palíndromo

      #Resposta do Guanabara

    #APOS A SOPA #A SACADA DA CASA #A TORRE DA DERROTA #O LOBO AMA O BOLO #ANOTARAM A DATA DA MARATONA #ARARA #OSSO

'''frase = str(input('Digite uma frase:  ')).strip().upper() #strip tira os espaços #upper coloca tudo em maiúscula
palavras = frase.split() #split divide as palavras
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1 ): #len(junto) ele pega o num total letras, vai até a penúltima q é -1, vai até a -1 q é antes da primeira q é zero, e vai voltando uma letra.
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

#Agora um macete de fatiamento
#No exemplo abaixo não teremos a linha 25 e 26, q é a linha do for.

frase = str(input('Digite uma frase:  ')).strip().upper() #strip tira os espaços #upper coloca tudo em maiúscula
palavras = frase.split() #split divide as palavras
junto = ''.join(palavras)
inverso = junto[::-1] #: início, e os outros dois pontos : o fim, e o -1 de trás para frente
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')