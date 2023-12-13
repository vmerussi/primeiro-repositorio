#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

#t = int(input('Digite um número: '))
#print (t, 'x 1 =', t*1)
#print (t, 'x 2 =', t*2)
#print (t, 'x 3 =', t*3)
#print (t, 'x 4 =', t*4)
#print (t, 'x 5 =', t*5)
#print (t, 'x 6 =', t*6)
#print (t, 'x 7 =', t*7)
#print (t, 'x 8 =', t*8)
#print (t, 'x 9 =', t*9)
#print (t, 'x 10 =', t*10)


#Solução do Prof: Guanabara

t= int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(t, 1, t*1))
print('{} x {:2} = {}'.format(t, 2, t*2))
print('{} x {:2} = {}'.format(t, 3, t*3))
print('{} x {:2} = {}'.format(t, 4, t*4))
print('{} x {:2} = {}'.format(t, 5, t*5))
print('{} x {:2} = {}'.format(t, 6, t*6))
print('{} x {:2} = {}'.format(t, 7, t*7))
print('{} x {:2} = {}'.format(t, 8, t*8))
print('{} x {:2} = {}'.format(t, 9, t*9))
print('{} x {:2} = {}'.format(t, 10, t*10))
print('-' * 12)