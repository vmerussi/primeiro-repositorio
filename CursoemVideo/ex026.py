#desafio 26

#Faça um programa que leia uma frase pelo teclado e mostre:

#- Quantas vezes aparece a letra "A".
#- Em que posição ela aparece pela primeira vez.
#- Em que posição ela aparece a última vez.

#frase.count('a', 0, :)
#frase.find('deo') ele mostra onde começou o 'deo'
#frase[15:]
#frase = 'Curso em Vídeo Python'
#print(frase[13:])
#frase = 'Curso em Vídeo Python' Aqui ele conta quantas letras o tem e transforma elas em maiúsculas.
#print(frase.upper().count('O'))

#frase = str(input('Digite uma frase: ')).upper().strip()
#print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
#print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
#print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

#ex 27

#nome = str(input('Digite seu nome completo: ')).strip()
#nome = nome.split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))

#Aula 10 - Condições

#Conjunto de Passos = algoritimo
# Quando existem mais de uma opção para chegar no mesmo resultado, podemos apliacar as condições da seguinte forma:
# se carro.esquerda() senão
#Representação estruturada ou identada
#exemplo

#carro.siga()
#se carro.esquerda()
#    carro.siga()
#    carro.direita()
#    carro.siga()
#    carro.direita()
#    carro.esquerda()
#    carro.siga()
#    carro.direita()
#    carro.siga()
#senão
#    carro.siga()
#    carro.esquerda()
#    carro.siga()
#    carro.esquerda()
#    carro.siga()
# carro.pare()

#Estrutura Condicional

#se carro.esquerda()                    if carro.esquerda():
  # bloco_V_                                bloco True
#senão                                  else:
  # bloco_F_                                bloco False

#Em uma condição, ou um bloco é executado (verdadeiro), ou o outro bloco é executado (falso)
#if carro.esquerda():
#    bloco True
#else:
#    bloco False

#Outro exemplo
#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <=3:
#    print('carro novo')
#else:
#    print('carro velho')
#print('--FIM--')

#Outro exemplo usando somente 3 linhas

# tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <=3 else 'carro velho')
#print('--FIM--')

#Prática

#nome = str(input('Qual é o seu nome? '))
#if nome == 'Gustavo':
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é tão normal!')
#print('Bom dia, {}!'.format(nome))

#NUNCA ESQUECER OS DOIS PONTOS :
#Condição Composta
#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1 + n2)/2
#print('A sua média foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('Sua média foi boa! PARABÉNS!')
#else:
#    print('Sua média foi ruim! ESTUDE MAIS!')

#Agora usando Parabéns e Estude Mais de forma simplificada

#Condição Simples
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(media))
print('PARABÉNS' if media >=6 else 'ESTUDE MAIS!')

#Desafio 028
# Escreva um progrma que faça o computador "pensar" em um número inreiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Desafio 029
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

#Desafio 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#Desafio 031
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

#Desafio 032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#Desafio 033
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Desafio 034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

#Desafio 035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 