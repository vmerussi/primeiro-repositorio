#print('Desafio 03')
import random
#n = input('Digite algo: ')
#print('O tipo primitivo desse valor é: ', type(n))
#print('Só tem espaços? ', n.isspace())
#print('É um número? ', n.isnumeric())
#print('É alfabético? ', n.isalpha())
#print('É alfanumérico? ', n.isalnum())
#print('Está em maiúscula? ', n.isupper())
#print('Está em minúscula?', n.islower())
#print('Está capitalizada? ', n.istitle())

#t= int(input('Digite um número para ver sua tabuada: '))
#print('-' * 12)
#print('{} x {:2} = {}'.format(t, 1, t*1))
#print('{} x {:2} = {}'.format(t, 2, t*2))
#print('{} x {:2} = {}'.format(t, 3, t*3))
#print('{} x {:2} = {}'.format(t, 4, t*4))
#print('{} x {:2} = {}'.format(t, 5, t*5))
#print('{} x {:2} = {}'.format(t, 6, t*6))
#print('{} x {:2} = {}'.format(t, 7, t*7))
#print('{} x {:2} = {}'.format(t, 8, t*8))
#print('{} x {:2} = {}'.format(t, 9, t*9))
#print('{} x {:2} = {}'.format(t, 10, t*10))
#print('-' * 12)

#t = int(input('Digite um número para ver a sua tabuada: '))
#print('-' * 12)
#print('{} x {:2} = {}'.format(t, 1, t*1))


#Solução do Guanabara
#num = int(input('Digite um número para ver sua tabuada: '))
#print('{} x {} = {}'.format(num, 1, num*1))
#print('{} x {} = {}'.format(num, 2, num*2))
#print('{} x {} = {}'.format(num, 3, num*3))
#print('{} x {} = {}'.format(num, 4, num*4))
#print('{} x {} = {}'.format(num, 5, num*5))
#print('{} x {} = {}'.format(num, 6, num*6))
#print('{} x {} = {}'.format(num, 7, num*7))
#print('{} x {} = {}'.format(num, 8, num*8))
#print('{} x {} = {}'.format(num, 9, num*9))
#print('{} x {} = {}'.format(num, 10, num*10))

#real = float(input('Digite a quantia em carteira? R$: '))
#dolar = real / 4.80
#print('Com R${}, você pode comprar Us${}'.format(real, dolar))

#preco = float(input('Qual é o valor do produto? R$ '))
#novo = preco - (preco * 5 / 100)
#print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))

#preco = float(input('Qual o preço do produto? R$ '))
#desconto = float(input('Qual o desconto? '))
#descontado = preco - (preco*desconto/100)
#print('O valor com desconto é: {}'.format(descontado))

#salario = float(input('Digite o salário atual: '))
#novo = salario + (salario * 15 / 100)
#print('O salário {} com reajuste de 15%, será de {}'.format(salario, novo))

#celsius = float(input('Digite a temperatura em graus celsius: '))
#farenheit = (celsius * 1.8) + 32
#print('A temperatura de {} Celsius corresponde a {} em Farenheits'.format(celsius, farenheit))

# Foi a minha solução mas o Guabanara fez outra conta com divisão por 5 e mesmo buscando no Google não encontrei.
#ex:
#c = float(input('Informe a temperatura em C: '))
#f = ((9 * c) / 5) + 3 2
#print('A temperatura de {}C corresponde a {}F!'.format(c, f))

# essa conta dá certo tb. O que eu achei de fórmula no Google foi:
#(num Celsius, ex 40graus Celsius x 9/5)+ 32 = 104F
# Nesse caso n~ao precisa colocar parênteses pq a ordem de prededência da expressão é exatamente a ordem que os operadores aparecem.


#from math import sqrt
#num = int(input('Digite um número: '))
#raiz =  sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#import random
#num = random.random()
#print(num)

#import emoji
#print(emoji.emojize("Olá, Mundo : :melting_face:", language='alias'))

#from math import trunc
#num = float(input('Digite um número: '))
#print('O número digitado foi {}, e a sua porção inteira é {}'.format(num, trunc(num)))
#outro exemplo
#import math
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
#outro exemplo sem importar a biblioteca matemática ( ou sem importar módulos )
#'''from math import trunc
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#ex017CatetoseHipotenusa
#catetooposto = float(input('Comprimento do cateto oposto: '))
#catetoadjacente = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = (catetooposto ** 2 + catetoadjacente ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
#outraformaimportandoaclassemath
#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = math.hypot(co, ca)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
#Como estamos usando só um método que é o hypot, dá pra fazer dessa forma tb:
#from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = hypot(co, ca)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#seno, cosseno e tangente
#import math ( no modulo math usamos os metodos:  radians, sin, cos, tan
#angulo = float(input('Digite o ângulo que você deseja: '))
#seno = math.sin(math.radians(angulo))
#print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
#cosseno = math.cos(math.radians(angulo))
#print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
#tangente = math.tan(math.radians(angulo))
#print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#outro exemplo simplificado ( Nesse caso tira todas as referências de math, pq os modulos vão ficar todos juntos no from math.
#Pq sempre que eu importo dessa maneira, eu não preciso mais referenciar o módulo que eu importei.)

#from math import radians, sin, cos, tan
#angulo = float(input('Digite o ângulo que você deseja: '))
#seno = sin(radians(angulo))
#print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
#cosseno = cos(radians(angulo))
#print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
#tangente = tan(radians(angulo))
#print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#import random
#primeiro = str(input('Primeiro aluno: '))
#segundo = str(input('Segundo aluno: '))
#terceiro = str(input('Terceiro aluno: '))
#quarto = str(input('Quarto aluno: '))
#lista = [primeiro, segundo, terceiro, quarto]
#escolhido = random.choice(lista)
#print('O aluno escolhido foi {}'.format(escolhido))

#Outra forma de fazer sorteio aleatório no código mas usando from. Mas esse sorteio sendo de 1 pessoa.

from random import choice

#pokemon1 = input('Digite o nome do primeiro Pokemon: ')
#pokemon2 = input('Digite o nome do segundo Pokemon: ')
#pokemon3 = input('Digite o nome do terceiro Pokemon: ')
#pokemon4 = input('Digite o nome do quarto Pokemon: ')
#lista = [pokemon1, pokemon2, pokemon3, pokemon4]
#escolhido = random.choice(lista)
#print('O aluno escolhido foi {}'.format(escolhido))


#Para fazer sorteio aleatório misturando os nomes dos alunos usamos o shuffle ao invés de choice.
import random
#aluno1 = input('Primeiro aluno: ')
#aluno2 = input('Segundo aluno: ')
#aluno3 = input('Terceiro aluno: ')
#aluno4 = input('Quarto aluno: ')
#lista = [aluno1, aluno2, aluno3, aluno4]
#random.shuffle(lista)
#print('A ordem de apresentação do trabalho será ')
#print(lista)

#Para fazer usando from

#from random import shuffle
#aluno1 = input('Primeiro aluno: ')
#aluno2 = input('Segundo aluno: ')
#aluno3 = input('Terceiro aluno: ')
#aluno4 = input('Quarto aluno: ')
#lista = [aluno1, aluno2, aluno3, aluno4]
#shuffle(lista)
#print('A ordem de apresentação do trabalho será: ')
#print(lista)

