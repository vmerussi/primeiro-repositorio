#Exercício 051
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA ( Progressão Aritimética ).
#No final, mostre os 10 primeiros termos dessa progressão.

#primeiro = int(input('Primeiro termo: '))
#razao = int(input('Razão: '))
#for c in range(1, 10, 1):
#    print('{} '.format(c), end=' ')
#print('Acabou!')

#Para calcular o décimo termo tem uma fórmula:

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end=' ')
print('Acabou!')