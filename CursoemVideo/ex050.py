#Exercício 050 - Aula 13 Mundo 2
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0 #acumulador
cont = 0 #contador
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num #seleciona essas 2 linhas e aperta tab para identar, ou para desfazer shift + tab e ele volta.
        cont += 1 #Cont é de contador
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma ))


