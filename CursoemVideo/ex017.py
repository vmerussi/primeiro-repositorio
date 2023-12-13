#Desafio017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi =  (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

# import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = math.hypot(co, ca)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#hypot Significa hipotenusa.
#Tivemos só que importar essa funcionalidade, pq ela não vem por padrão, e nem todos os programas eu vou ter cálculo de hipotenusa.
#Então ele coloca esse método dentro do módulo math, e aí eu importo se eu quiser.

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Nesse caso como estamos usando só 1 método, ao invés de usar math import vamos usar: from math import hypot.
#Aqui foram 4 exemplos de como resolver usando os métodos da Aula 08.
