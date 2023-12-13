#Desafio 031
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

kmPercorrido = int(input('Qual a distância percorrida na viagem? '))
precoPassagem = 0.50 * kmPercorrido
viagemLonga = 0.45 * kmPercorrido
if kmPercorrido <= 200:
    print('A distância percorrida foi de {}, totalizando {}'.format(kmPercorrido, precoPassagem))
else:
    print('A distância percorrida foi de {}, totalizando {}'.format(kmPercorrido, viagemLonga))


    # Jeito do Guanabara
    #distancia = float(input('Qual é a distância da sua viagem? '))
    #print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
#if distancia <= 200:
    #preço = distancia * 0.50
#else:
    #preço = distancia * 0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#Outro se simplificado:

#distancia = float(input('Qual é a distância da sua viagem? '))
#print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
#preço = distancia * 0.50 if distancia <= 200 else distância * 0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(preço))