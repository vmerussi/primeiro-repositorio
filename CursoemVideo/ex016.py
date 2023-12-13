# Desafio
# 016) Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

#Meu jeito:
#from math import trunc
#num = float(input('Digite um número: '))
#pi = trunc(num)
#print('O valor digitado foi {} e a sua porção inteira do número digitado é {}'.format(num, pi))

#Outra forma do Guanabara

#import math
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

from math impor trunc
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

num = float(input('Digite o valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#nesse caso, ao invés de colocar trunc, pode colocar int ( inteiro ), que tb é um outro jeito sem precisar do trunc.

