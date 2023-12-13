#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#n = (int(input('Digite um valor: ')))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('Um número {} seu dobro é {}, seu triplo {}, a raiz quadrada é {:.2f}'.format(n, d, t, r))

#Outras formas de fazer:

# n = int(input('Digite um número: '))
# print('O dobro de {} vale {}.'.format(n, (n*2)))
# print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

# A raiz quadrada dá pra fazer de outro jeito, com a função de power, função de potência:

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))