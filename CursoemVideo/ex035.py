#Desafio 035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# O maior lado é menor que a soma dos outros dois
# a < b + c
# b < a + c
# c < a + b

a = float(input('Primeiro segmento: '))
b =  float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triângulo!')
else:
     print('Os segmentos acima não podem formar triângulo!')

#and diferente de or

#Até aqui estudamos:
# - Fundamentos de Python
# - Como ele funciona
# - Como instalar
# - Os primeiros comandos básicos
# - Operadores aritiméticos, lógicos e relacionais
# - A utilização de módulos e estruturas condicionais básicas

