#Desafio 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


numeroescolhido = int(input('Digite um número: '))
if numeroescolhido % 2 == 0:
    print('O número é PAR!')
else:
    print('O número {:.2f} é ÍMPAR!'.format(numeroescolhido))

#Jeito do Guanabara
#numero = int(input('Me diga um número qualquer: '))
#resultado = numero % 2
#if resultado == 0:
    #print('O número {} é PAR!'.format(numero))
#else:
    #print('O número {} é ÍMPAR'.format(numero))