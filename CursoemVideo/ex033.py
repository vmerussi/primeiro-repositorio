# Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# primeiro = int(input('Digite o primeiro número: '))
# segundo = int(input('Digite o segundo número: '))
# terceiro = int(input('Digite o terceiro número: '))
# lista = [primeiro, segundo, terceiro]
# print('O maior número é {}'.format(max(lista)))
# print('O menor número é {}'.format(min(lista)))

# Guanabara's Way

# Primeiro jeito q as pessoas pensam qdo programam:

# primeiro = int(input('Primeiro valor: '))
# segundo = int(input('Segundo valor: '))
# terceiro = int(input('Terceiro valor: '))
# if primeiro<segundo and primeiro<terceiro:
#    menor = primeiro
# if segundo<terceiro and segundo<primeiro:
#    menor = segundo
# if terceiro<primeiro and terceiro<segundo:
#    menor = terceiro
# ---------------------------------------------------------------------------------------
# Segundo jeito, mas agora do Guanabara, simplificando, considerando 1 menor e depois considrando um maior

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
