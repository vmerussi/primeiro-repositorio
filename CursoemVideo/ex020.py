#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada.

#import random
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)
#print('A ordem de apresentação será {}'.format(lista))

#Outras formas de fazer:

#import random
#print('SERÁ SORTEADA A ORDEM DOS ALUNOS PARA APRESENTAÇÃO DOS TRABALHO REALIZADO')
#aluno1 = str(input('NOME DO ALUNO: '))
#aluno2 = str(input('NOME DO ALUNO: '))
#aluno3 = str(input('NOME DO ALUNO: '))
#aluno4 = str(input('NOME DO ALUNO: '))
#população = (aluno1,aluno2,aluno3,aluno4)
#embaralhar = random.sample(população, k=4)
#print('A ORDEM DO SORTEIO SERÁ: {}'.format(embaralhar))

#METODO CURTO
#from random import sample
#aluno1 = input('NOME DO ALUNO: ') #não é necessário especificar string (str)
#aluno2 = input('NOME DO ALUNO: ')
#aluno3 = input('NOME DO ALUNO: ')
#aluno4 = input('NOME DO ALUNO: ')
#lista = [aluno1,aluno2,aluno3,aluno4]
#sorteio = sample(lista, k=4) #o k significa a quantidade de membros do grupo que serão incluídos no sorteio, não pode ser maior do que o próprio grupo
#print(' A ORDEM DO SORTEIO SERÁ: {}'.format(sorteio))

#usando shuffle - embaralhar
#from random import shuffle
#aluno1 = str(input('NOME DO ALUNO: '))
#aluno2 = input('NOME DO ALUNO: ')
#aluno3 = input('NOME DO ALUNO: ')
#aluno4 = input('NOME DO ALUNO: ')
#lista = [aluno1,aluno2,aluno3,aluno4]
#shuffle(lista)  #é importante prestar atenção que usando o shuffle não é necessário criar uma especifiação.
#print('A ORDEM DE APRESENTAÇÃO SERÁ:')
#print(lista)

#import random
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)
#print('A ordem de apresentação será: ')
#print(lista)

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
