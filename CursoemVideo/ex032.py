#Desafio 032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#numeroDigitado = int(input('Digite o ano que deseja analisar: '))
#if numeroDigitado % 4 == 0:
    #print('O ano digitado {}, é BISSEXTO!'.format(numeroDigitado))
#else:
    #print('O ano digitado {}, não é BISSEXTO!'.format(numeroDigitado))

#Jeito do Guanabara (praticamente igual ao que eu fiz)
#ano = int(input('Que ano quer analisar? '))
#if ano % 4 == 0:
    #print('O ano {} é BISSEXTO')
#else:
    #print('O ano {} NÃO é BISSEXTO')

#Outro jeito do Guanabara:

#ano = int(input('Que ano quer analisar? '))
#if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    #print('O ano {} é BISSEXTO'.format(ano))
#else:
    #print('O ano {} NÃO é BISSEXTO'.format(ano))

#Outro jeito do Guanabara, mas analisar o ano atual que está na máquina.

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))


#Jeito da galera dos comentários

#from calendar import isleap
#from time import sleep
#from datetime import date
#ano = int(input('Digite um ano: '))
#print('analisando aqui...')
#sleep(0.5)
#if ano == 0:
   #ano = date.today().year
#if isleap(ano):
   #print(f'o ano de {ano} é bissexto')
#else:
   #print(f'o ano de {ano} NÃO é bissexto')