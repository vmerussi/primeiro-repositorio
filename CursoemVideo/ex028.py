#Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''from random import randint
from time import sleep
computador = randint(0, 5) # Esse comando faz o computador "PENSAR"
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))'''

#print('Pensei no número {}'.format(computador))
#escolhido = random.randint(lista)
#numeroAleatorio = int(input('Em que número eu pensei? '))
#print('O número escolhido foi {}'.format(escolhido))
#print('PARABÉNS, VC ACERTOU!' if numeroAleatorio = escolhido else 'NA TRAVE! TENTE NOVAMENTE!')
#Nesse caso é para aparecer o número q ele pensou.

from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
