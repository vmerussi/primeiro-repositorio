# Desafio 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O PRIMEIRO valor é maior')
elif b > a:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')

