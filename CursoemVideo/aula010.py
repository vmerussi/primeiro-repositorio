#Condições

'''carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()'''

#As condições carro.siga e carro.pare sempre vão acontecer

#if carro.esquerda():
#    bloco True
#else:
#    bloco False

#Ou o bloco verdadeiro será executado ou o bloco Falso será executado, NUNCA os 2 ao mesmo tempo.
#If sempre para estrutura condicional simples, e if else para estrutura condicional composta.

#Tudo q estiver identado está dentro de uma condição, e tudo q está fora, ou seja, alinhado a esquerda, vai acontecer todas as vezes.

#if estrutura simples
#if else estrutura composta

#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <= 3:
#    print('carro novo')
#else:
#    print('carro velho')
#print('--FIM--')

#Agora mesmo resultado, mas na condição simplificada, com menos linhas.

#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo<= 3 else 'carro velho')
#print('--FIM--')

#nome = str(input('Qual é o seu nome? ')) #Nesse caso não precisa de else, pq a condição é somente se o nome for Gustavo.
#if nome == 'Gustavo':                    #Estrutura condicional simples
#    print('Que nome lindo você tem!')
#print('Bom dia, {}!'.format(nome))

#nome = str(input('Qual é o seu nome? '))
#if nome == 'Gustavo':
#    print('Que nome lindo você tem!')
#else:                                    #Estrutura condicional composta
#    print('Seu nome é tão normal!')
#print('Bom dia, {}!'.format(nome))

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1 + n2) / 2
#print('A sua média foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('Sua média foi boa! PARABÉNS!')
#else:                                          #Condição Composta
#    print('Sua média foi ruim! ESTUDE MAIS!')

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1 + n2) / 2
#print('A sua média foi {:.1f}'.format(m)) #Agora utilizando o if simplificado, Condição Simplificada
#print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!' )

#Nunca esqueça dos dois pontos :

# Ex 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# #pelo computador.
# # O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador)'''

#print('Pensei no número {}'.format(computador))
#escolhido = random.randint(lista)
#numeroAleatorio = int(input('Em que número eu pensei? '))
#print('O número escolhido foi {}'.format(escolhido))
#print('PARABÉNS, VC ACERTOU!' if numeroAleatorio = escolhido else 'NA TRAVE! TENTE NOVAMENTE!')
#Nesse caso é para aparecer o número q ele pensou.

# Ex 29 - Escreva um programa que leia a velocidade de um carro.
# #Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# #A multa vai custar R$7,00 por cada Km acima do limite.

'''velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('MULTADO! Você ultrapassou o limite permitdo que é 80Km/h!')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')'''

#Ex 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#numero = int(input('Digite um número para saber se ele é par ou ímpar: '))
#resto = numero % 2

#if resto == 0:
#    print('O número {} é PAR'.format(numero))
#else:
#    print(' O número {} é ÍMPAR!'.format(numero))

#Ex 031 - #Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

#distancia = float(input('Qual é a distância da sua viagem? '))
#print('Você está prestes a começar uma viagem de {}'.format(distancia))
#if distancia <= 200:
#    preco = distancia * 0.50
#else:                          #Estrutura Composta
#    preco = distancia * 0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(preco))

#distancia = float(input('Qual é a distância da sua viagem? '))
#print('Você está presteas a começar uma viagem de {}Km.'.format(distancia))
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 #Estrutura Simplificada
#print('E o preço da sua passagem será de R${:.2f}'.format(preco))

#Ex 032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#from datetime import date #importar módulo, biblioteca datetime, date vai trabalhar só com a data.
#ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
#if ano == 0:
#    ano = date.today().year
#if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
#    print('O ano {} é BISSEXTO'.format(ano))
#else:
#    print('O ano {} NÃO É BISSEXTO'.format(ano))

#Ex 033
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''

#Ex 034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

'''salario = float(input('Qual é o salário do funcionário? '))
if salario <=1250.00:
    novo = salario + ( salario * 15 / 100 )
else:
    novo = salario + ( salario * 10 / 100 )
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))'''

#Desafio 035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Esse código abaixo eu fiz sozinha
'''a = float(input('Primeiro segmento: '))
b =  float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triângulo!')
else:
     print('Os segmentos acima não podem formar triângulo!')'''

#Código do Guanabara

'''print('Analisador de Triângulos')
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')'''





















