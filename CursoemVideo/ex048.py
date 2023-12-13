#Exercício 048
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#for n in range(1, 501, 2):
#    if n % 3 == 0:
#    print(n, end=' ') #Essa linha faz uma listagem, mas nesse caso queremos a soma, usando o conceito de acumulador. Acumulador soma.
#print('Acabou')

#soma = 0 #soma é o acumulador
#cont = 0 #contador
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        cont = cont + 1
#        soma = soma + c #Soma é o que ela tem + o número
#print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
#Resposta: A soma de todos os 83 valores solicitados é 20667.

#soma = 0 #soma é o acumulador
#cont = 0 #contador
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        soma = soma + c #Soma é o que ela tem + o número
#        cont = cont + 1 #Agora invertendo essa linha, e colocando soma na linha de cima.
#print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
#Ao executar o resultado é o mesmo do código acima: A soma de todos os 83 valores solicitados é 20667.

#soma = 0 #soma é o acumulador
#cont = 0 #contador
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        soma = soma + c #Soma é o que ela tem + o número
#    cont = cont + 1 #Agora identando ou alinhando à esquerda, ele vai parar de contar só os números q são divididos por 3, e vai começar a contar todos os números.
#print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
#A soma de todos os 250 valores solicitados é 20667.

#Outra forma simplificada desse mesmo código acima:
#soma = 0
#cont = 0
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        soma += c
#        cont += 1
#print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
#Resposta: A soma de todos os 83 valores solicitados é 20667

