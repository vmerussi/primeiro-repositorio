#Desafio 47
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
#Abaixo 3 formas de resolver:

#for n in range(1, 51):
#    if n % 2 == 0:
#        print(n, end=' ')
#print('Acabou')

#for n in range(1, 51):
#    print('.', end='')
#    if n % 2 == 0:
#        print(n, end=' ')
#print('Acabou')
# Essa é outra alternativa de resposta desse laço: ..2 ..4 ..6 ..8 ..10 ..12 ..14 ..16 ..18 ..20 ..22 ..24 ..26 ..28 ..30 ..32 ..34 ..36 ..38 ..40 ..42 ..44 ..46 ..48 ..50 Acabou

#for n in range(2, 51, 2):
#    print('.', end='')
#    print(n, end= ' ') #Dessa vez não tem o if, pq já sabemos q uma das vezes q ele faz o laço não é importante, tirando o if n % 2 == 0 e deixando o print dessa linha
#print('Acabou')
# A resposta desse laço é: .2 .4 .6 .8 .10 .12 .14 .16 .18 .20 .22 .24 .26 .28 .30 .32 .34 .36 .38 .40 .42 .44 .46 .48 .50 Acabou
# Nesse caso só tem 1 pontinho pq ele fez a metade das repetições, ele ocupou o seu processador metade do tempo

#Outra forma mais simples, com menos linha, mas o mesmo resultado:
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
# Resposta: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 Acabou

# Não é o número de linhas que influencia, e sim o número de iterações, o número de laços. 