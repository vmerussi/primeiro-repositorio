#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))


#Considereções sobre o random, e alugmas finalidades de uso:
#1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
#2. Você quer fazer um sorteio entre 300 nomes em uma lista de nomes
#3. Você quer escolher aleatóriamente um número de 10-100
#4. Você quer escolher uma carta aleatóriamente dentro de um baralho
#5. Você quer gerar nomes de usuário aleatóriamente
#6. Você quer gerar senhas seguras


#import random

#print(random.random()) # Valor 0.0 até 1.0
#print(random.uniform(4,10)) # Valor decimal do mínimo ao máximo
#print(random.randint(12,55)) #Valor inteira do mínimo ao máximo

cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores)) # Escolher uma opção dentro de uma fonte

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho)