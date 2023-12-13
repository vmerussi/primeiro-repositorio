# desafio 23

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# Ex:
# Digite um número: 1834

# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

import random

#numero = random.randrange(0, 9999)
#escolhido = input('Digite um número de 0 a 9999: ')
#milhar = [0]
#centena = [1]
#dezena = [2]
#unidade = [3]
#print('{}, {}, {}, {}'.format(milhar, centena, dezena, unidade))








#num = int(input('Informe um número: '))
#n = str(num)
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

#Se vc quiser colocar o número 123 por exemplo vai dar erro, pq a gnt não usou os 4 dígitos. Nesse caso seria necessário usar estrutura de repetição.
#Uma forma matemática de fazer isso. Nesse outro código vamos tirar a lista, e a conversao para string(que não é a melhor maneira de trabalhar com string
#nesse momento).
#Vamos começar calculando a unidade e fazendo a divisao inteira por 1.
#u será o resto da divisão, então o num digitado dividido por 1, depois divide por 10, e pega o resto da divisão, e esse resto q sobrou é a minha unidade.
#d nesse caso se dividirmos somente por 10 ele vai mostrar 3 num como resultado. Então vc divide por 10 e pega o resto: 10 % 10, e pega 1 digito.
#Se for dividido por 100 ele vai pegar 2 dígitos.
#Mesma coisa na centena e milhar, divide por 10 pra pegar 1 digito. E nesse código vc consegue colocar 2 números, q ele separa direitnho ( unidade e dezena ).

#num = int(input('Informe um número: '))
#u = num // 1 % 10 ( Fazendo a correlação de acordo com cada tipo: unidade 1 %, dezena 10 %, centena 100 %, milhar 1000 % .
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(u))
#print('Dezena: {}'.format(d))
#print('Centena: {}'.format(c))
#print('Milhar: {}'.format(m))

#Nesse caso se vc digitar 12, como não tem milhar nem centena aparecerá 0 como resultado nos 2; dezena 1 e unidade 2.

#num = int(input('Informe um número: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(u))
#print(('Dezena: {}'.format(d)))
#print('Centena: {}'.format(c))
#print('Milhar: {}'.format(m))     Esse fiz sozinha
























