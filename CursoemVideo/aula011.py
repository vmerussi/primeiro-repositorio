#Aula 11 - Cores no terminal
import random

#ANSI Padrão de normalização internacional, ou Escape Sequence que funciona em vários ambientes.
# Vamos usar dentro do terminal, então tudo começa com contra barra ( barra invertida ) \ 033 e colchetes [ e fechar esse código com a letra m ( \033[m ).
# Entre esse colchete e a letra m vc vai colocar o código da cor, e não é hexadecimal, ou decimal, é um código maluco, com poucas cores, mas que vão ser
# suficientes pra gnt fazer as nossas primeiras brincadeiras com o Python. Esse código vai dentro do Python, C, e mais um monte de linguagens.
#O código que funciona melhor para o Python é o 033, então sempre q for representar uma cor em Python, você vai começar com \033[m.
#Entre o colchete e o m vc vai preencher com coisas. Essas coisas podem ser nenhum código, 1 código, 2 códigos, ou 3 códigos.
#O primeiro código é o código do comportamento, é o código do estilo ( style ), em seguida coloca ponto e vírgula, e colocar o segundo código, que é
# o código do texto, e por final vc vai colocar o último código, que é o código do background, que é a cor de fundo.
#Então basicamente vc vai indicar o estilo(negrito, sublinhado, cor do texto, e cor do fundo ). Mas vc pode colocar em qualquer ordem, pq vc vai entender
#que existe diferenciação numérica entre código de estilo, código de texto, e código de fundo. Vamos dar um exemplo:
# \033[0;33;44m ( 0 style, 33 text, 44 back )
#0 significa sem estilo, ponto e vírgula ; código do texto 33, código de fundo 44 e a letra m ( estilo, texto e fundo ).
#Existem vários códigos para estilo, mas o q vão funcionar melhor para o Python são 0147.
# 0 None ( Sem estilo nenhum. Vc pode colocar 0 ou não colocar nada )
# 1 Bold ( Coloca o texto em Negrito )
# 4 Underline ( Coloca o texto em Sublinhado )
# 7 Negative ( Ele inverte as configurações: o q vc colocou pra fundo vai para letra, o q estiver em letra vai para fundo.
# A Cor do texto sempre começa com o número 3, começa no 30 e vai até o 37.
# No Backgound é a mesma coisa do Text, só que as cores começam no 40 e vai até o 47.
#As cores são do padrão ANSI. Aos 08:40 guardei o Guanabara no whats com o print das cores e estilos do Python.

# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m #só fazendo isso ele volta para o padrão do terminal, que é letra cinza, fundo preto.
# \033[7;30m #usa o código 7 que é o de inversão, então ele pega o fundo que é preto e joga na letra, faz a letra preta, e a letra q é branca vira para
# o fundo, vai ficar com o fundo branco.
#Colorize pesquisar: módulo q trabalha com mto mais opções de cores no terminal, inclusive representação em hexadecimal.
# Vamos usar a sequência de escape do padrão ANSI.

#Prática do Sistema de Cores Python
#print('\033[1;31;43mOlá, Mundo!\033[m') #colocando contra barra \ no final vc tira as formatações seguintes ao texto ou frase que vc digitou.
#print('\033[4;30;45mOlá, Mundo!\033[m')      #sublinhado letra branca
#print('\033[37mOlá, Mundo!\033[m')
#print('\033[7;30mOlá, Mundo!\033[m') #estou invertendo, fundo branco letra preta
#print('\033[7;33;44mOlá, Mundo!\033[m') #inverte as cores q foram colocadas no comando, e vira letra azul, fundo amarelo.
#print('\033[0;33;44mOlá, Mundo!\033[m') #letra amarela fundo azul

#a = 3
#b = 5
#print('Os valores sã0 \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

#Agora exemplo usando format do print para facilitar

#nome = 'Guanabara'
#print('Olá! Muito prazer em te conhecer, {}{}!!!'.format('\033[4;34m', nome))

#Outro exemplo de coisas q vamos usar mais pra frente
#nome = 'Guanabara'
#cores = {'limpa': '\033[m',
#         'azul': '\033[34m',
#         'amarelo': '\033[33m',
#         'pretoebranco': '\033[7;30m'}
#print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
#print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))


#Exercícios

# Nível fácil : aplicar em uns 10 dos 35 exercícios que o Guanabara passou e colocar cores
# Nível difícil : nos 35 exercícios que ele passou criar um sistema de cores para eles.
# Repetindo o código desde o começo vc acaba memorizando e aprendendo

#Exercício 001
#print('\033[4;30;46mOlá, Mundo!\033[m')

#Exercício 002
#nome = input('\033[1;36;40mDigite seu nome: \033[m')
#print('\033[4;35;40mÉ um prazer te conhecer, {}!\033[m'.format(nome))

#Exercício 003
#n1 = int(input('\033[4;35;40mDigite um número: \033[m'))
#n2 = int(input('\033[1;30;45mDigite mais um número: \033[m'))
#s = n1 + n2
#print('\033[7;36;40mA soma entre {} e {} vale {}\033[m'.format(n1, n2, s))

#Exercício 004
#a = input('Digite algo: ')
#print('O tipo primitivo desse valor é ', type(a))
#print('É alfanumérico? ', a.isalnum())
#print('É alfabético?', a.isalpha())
#print('É um número? ', a.isnumeric())
#print('É título? ', a.istitle())
#print('É minúsculo? ', a.islower())
#print('Só tem espaços? ', a.isspace())
#print('É decimal? ', a.isdecimal())
#print('É maiúsculo? ', a.isupper())
#print('É printável? ', a.isprintable())

#Exercício 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#n = int(input('Digite um número: '))
#s = n + 1
#a = n - 1
#print('O número {} tem como seu sucessor o número {} e o antecessor {}'.format(n, s, a))

#Outro jeito

#n = int(input('Digite um número: '))
#print('Analisando o valor de {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

#Quanto menos variáveis, mais memória no seu dispositivo. Agora se mais pra frente vc precisasse do sucessor e antecessor,
#vc seria obrigado a colocar.

#Exercício 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#n = int(input('Digite um número: '))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('O dobro de {} vale {}.'.format(n,d))
#print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

#Outro jeito

#n = int(input('Digite um número: '))
#print('O dobro de {} vale {}.'.format(n, (n*2)))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

#E a raiz quadrada pode ser feita de outra forma, através da função de power ou potência:

#print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, 1/2)))
                                                                                                #base(n) e expoente (1/2)
#Raiz quadrada: numero **(1/2)
#Raiz cúbica: numero **(1/3

#Exercício 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
#n1 = float(input('Primeira nota: '))
#n2 = float(input('Segunda nota: '))
#media = (n1 + n2) / 2
#print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))

#Exercicio 008 -  Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros
#medida = float(input('Uma distância em metros: '))
#cm = medida * 100
#mm = medida * 1000
#print('A medida de {:.0f}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

#Exercício 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#n = int(input('Digite um número para ver a sua tabuada: '))
#print('{} x {} = {}'.format(n, 1, n*1))
#print('{} x {} = {}'.format(n, 2, n*2))
#print('{} x {} = {}'.format(n, 3, n*3))
#print('{} x {} = {}'.format(n, 4, n*4))
#print('{} x {} = {}'.format(n, 5, n*5))
#print('{} x {} = {}'.format(n, 6, n*6))
#print('{} x {} = {}'.format(n, 7, n*7))
#print('{} x {} = {}'.format(n, 8, n*8))
#print('{} x {} = {}'.format(n, 9, n*9))
#print('{} x {} = {}'.format(n, 10, n*10))

#3 formas de solucionar o exercício. Ao invés de ficar digitando format, o f antes da primeira aspa faz a mesma função e roda operações matemáticas.
#t = int(input('Digite um número '))
#r = t*1, t*2, t*3, t*4, t*5, t*6, t*7, t*8, t*9, t*10
#print(r)
#print('{} x {} = {}'.format(t, 1, t*1))
#print('{} x {} = {}'.format(t, 2, t*2))
#print('{} x {} = {}'.format(t, 3, t*3))
#print('{} x {} = {}'.format(t, 4, t*4))
#print('{} x {} = {}'.format(t, 5, t*5))
#print('{} x {} = {}'.format(t, 6, t*6))
#print(f'{t} x {7} = {t*7}')
#print(f'{t} x {8} = {t*8}')
#print(f'{t} x {9} = {t*9}')
#print(f'{t} x {10} = {t*10}')

#Exercício 10 - Conversão de real para dólar:

#real = float(input('Quanto dinheiro vc tem na carteira: R$ '))
#dolar = real / 3.27
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

#Exercicio 011 - Faça um programa q leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pintá-la, sabendo q cada litro de tinta pnta uma área de 2m2.

#larg = float(input('Largura da parede: '))
#alt = float(input('Altura da parede: '))
#area = larg * alt
#print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2.'.format(larg, alt, area))
#tinta = area / 2

#Exercício 012 - Faça um algotimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
#Cálculo de Porcentagem , desconto, multiplicação.
#preco = float(input('Qual é o preço do produto? R$ '))
#novo = preco - ( preco * 5 / 100)
#print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))

#Exercício 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#Outro cálculo com porcentagem

#salario = float(input('Qual é o salário do funcionário? R$ '))
#novo = salario + (salario * 15 / 100)
#print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))

#Exercício 014 - Escrreva um programa que converta uma temperatura digitada em C e converta para F.

#c = float(input('Temperatura em Celsius: '))
#f = c * 1.8 + 32
#print('{} Celsius corresponde a {} Farenheit'.format(c, f))

#Jeito do Guanabara

#c = float(input('Informe a temperatura em C: '))
#f = 9 * c / 5 + 32
#print('A temperatura de {}C corresponde a {}F!'.format(c,f))

#Exercício 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

#dias = int(input('Quantos dias alugados: '))
#km = float(input('Quantos Km rodados: '))
#pago = (dias * 60) + (km * 0.15)
#print('O total a pagar é de R${:.2f}'.format(pago))

#Aula 08 - Módulos

#import bebida ( esse abrange tudo q estiver dentro de bebida: leite, suco, água, refrigerante, etc... )
#ou
#from bebida import milk ( esse é mais específico para uma coisa q vc queira escolher )
#Ordem de Prededência: 1- () Parênteses, 2 - ** Potências, 3 - * / // % Multiplicação, Divisão, Divisão inteira, Resto da Divisão, 4 - + - soma e subtração.
#ceil - arredonda pra cima
#floor arredonda pra baixo
#trunc ele elimina da vírgula pra frente, sem arredondar
#pow potência - vai funcionar de forma semelhante aos 2 asteríscos
#sqrt square root - cálculo de raiz quadrada
#factorial - fatorial

#Se for importar 2 funcionalidades, pode fazer dessa forma: from math import sqrt, ceil

#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

#from math import sqrt, floor #apertando ctrl + espaço depois do from math import, aparecerá todas as funcionalidades disponíveis
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) #ou print('A raiz de {} é igual a {:.2f}'.format(num, floor()raiz))

#Exercício 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6

#from math import trunc
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num))) # esse resolvi sozinhaaaaaaaaaaa!!!!!!

#Respostas do Guanabara

#import math
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#Agora sem importar a biblioteca matemática

#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))


#Exercício 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

#Maneira tradicional matemática sem importação nenhuma
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(h))

#Agora com importação da classe math
#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = math.hypot(co, ca) #hypot significa hypotenusa
#print('A hipotenusa vai medir {:.2f}'.format(h))

#from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = hypot(co, ca) #hypot significa hypotenusa
#print('A hipotenusa vai medir {:.2f}'.format(h))

#Exercício 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno. cosseno e tangente desse ângulo.

#import math
#angulo = float(input('Digite o ângulo que você deseja: '))
#seno = math.sin(math.radians(angulo))
#print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
#cosseno = math.cos(math.radians(angulo))
#print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
#tangente = math.tan(math.radians(angulo))
#print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#from math import radians, sin, cos, tan
#angulo = float(input('Digite o ângulo que você deseja: '))
#seno = sin(radians(angulo))
#print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
#cosseno = cos(radians(angulo))
#print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
#tangente = tan(radians(angulo))
#print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#Exercício 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
#Aqui usamos random.choice para o sorteio aleatório.

'''import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''

'''from random import choice
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''

#Exercicio 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)'''

'''from random import shuffle
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)'''

#Exercício 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#Como existem módulos desenvolvido por programadores, existem várias maneiras de fazer isso, a maneira mais simples de fazer isso é utilizando um módulo bem famoso, chamado pygame

'''import pygame
pygame.init() #init é para iniciar o uso da biblioteca do pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

#Aula 09 - Manipulando texto

#fatiamento - frase Curso em Vídeo Python

# frase[9] identifica dentro da cadeia de caractere somente o caractere 9.
# A primeira letra é sempre 0, logo, a letra 9 na verdade é a décima letra. Ele tb diferencia maiúscula de minúscula.
# frase[9:13] - pega a partir da letra 9 até o 13, mas ele exclui o último aí ele vai pegar o 12 ( Víde ). inclui 9 remove o 13. Para pegar o 13 teria q ser [9:14]
# frase[9:21:2] vai do 9 ao 21 pulando de 2 em 2 letras. A frase ficaria: Vd o Pto
# frase[:5] ele vai do começo até a letra 5, excluindo a letra 5.Aqui ele fatiaria a palavra Curso.
# frase[15:] indicou o inicio até o final, qdo vc não onde é o final.
# frase[9::3] começa no 9 vai até o final, o o outro :3 é pra ele pular de 3 em 3 letras. o resultado mostrado é: V e P h.

# Análise - + usada. len vem de length q significa comprimento. Mostra qtos caracteres tem na frase.
# A frase utilizada acima tem 21 caracteres
# len(frase) mostra qtos caracteres tem na frase
# frase.count('o') o count vai contar quantas letras o ( entre aspas, senão ele vai pensar q é uma variável) tem na frase. Ele vai considerar somente no formato que vc colocou, maiúscula ou minúscula. Nessa frase, ele vai mostrar o valor de 3.
# frase.count('o, 0, 13') eu faço a contagem já com o fatiamento. Considera do 0 até o 13 ( mas vai até o 12 ), logo, só tenho 1 letra o, o resultado será 1.
# frase.find('deo') qtas vezes encontrou 'deo' , que nesse caso começou na posição 11. Resultado 11.
# frase.find('Android') qdo vc coloca uma string q não existe (Android), ele retorna o valor -1, significa q não foi encontrado, pois sabemos q ele começa na posição 0.
# 'Curso' in frase ( operador in) Existe curso in frase? ele vai retornar Verdadeiro (True). Isso não é funcionalidade, é um operador mas dá pra fazer análise.


# Transformação - Via de regra uma lista de string é imutável, não dá para mexer nela. Só é possível mudar ela através dos métodos:

# frase.replace('Python', 'Android') - ele procura a palavra Python e substitui por Android.
# frase.upper() O q já for maiúsculo ele mantém, o que não for ele troca.
# frase.lower() Mantém o q é minúsculo, e substitui o q estava em maiusculo para minúsculo.
# frase.capitalize() Joga todos os caracteres pra minúsculo, e só o primeiro caractere da string inteira que ele vai colocar em maiúsculo.
#Ex: frase Curso em Vídeo Python no capitalize:  Curso em vídeo python.
# frase.title() Analisa quantas palavras tem a string ( Curso em vídeo python ) nesse exemplo temos 4 palavras. Ele analisa onde tem espaço, fazendo uma quebra de palavra. Ele faz o capitalize palavra por palavra.
# cont. E coloca em maiúsculo a primeira letra de cada palavra. A frase Curso em vídeo python vai ficar: Curso Em Vídeo Python.
# frase.strip() Colocamos uma string com espaços propositalmente, com as casas vazias, pq? Qdo pessoas mais leigas ou mais velhas, ao se cadastrarem em algum site, ao invés de digitar no campo o que é solicitado, ex: digite seu nome: , ele não clica na caixa de
# texto e começa a digitar. A pessoa clica na caixa de texto, pra ver se está funcionando aperta espaço algumas vezes, e aí começa a digitar. Isso é tão comum, que as linguagens de programação tem funcionalidades internas pra remover esses espaços excedentes,
# no início e no final da cadeia. O frase.strip vai remover todos os espaços inúteis no início e no final da string, do meio vai ser mantido. O A que era caractere 3 vai passar a ser o 0, e a contagem vai continuar da mesma maneira que estava anteriormente.
# De forma similar, temos frase.rstrip(), r de right ou direita. Muitas funções dentro do Python q tratam strings tem a variação r. Tem algumas funcionalidades que você pode colocar um r na frente pra começar a tratar pela direita #ficaadica
# Ele vai remover os espaços do lado direito, ou seja, os últimos espaços. Então uma string q vai de 0 a 18, por exemplo, os 2 espaços excedentes ( 17, 18 ) são removidos, logo, o length será de 0 a 16, tendo um lenght de 17 caracteres.
# frase.lstrip() left esquerda - vai remover os espaços da esquerda ( os primeiros espaços ), mas vai manter os da direita.
# Remover só os espaços da direita: rstrip, só da esquerda lstrip, quer tirar todos os espaços indesejados nas extremidades strip.

# Divisão -

# frase.split() tem algumas funcionalidades a mais, mas q devo pesquisar. Por padrão, ele é feito em seus espaços. Ele pega onde tem espaços e cria uma divisão.
# Então cada palavra vai começar no 0. Ex Curso 0 até 4 , em 0 e 1. Ele refaz os índices. Cada palavra recebe uma indexação nova. Cada uma dessas palavras é colocada dentro de uma outra lista. Ele gera uma lista com todas as palavras de uma cadeia de caracteres.
# Ele vai dividir uma string em uma lista, onde cada elemento vai ser separado pelo seu splitador. Então fica assim:
# Curso  em  Vídeo  Python
# 01234  01  01234  012345
#   0     1    2       3

# Junção - se eu tenho nomes separados em listas, eu consigo utilizar o join pra juntar uma coisa na outra. Ele gera uma string única.

# '-'.join(frase) significa q vc vai juntar todos os elementos de frase, e vai usar esse separador '-'.
# Se vc quiser q só tenha espaço, é só colocar um espaço dentro da string ' '.

#Curso  em  Vídeo  Python
# 01234  01  01234  012345
#   0     1    2       3

# Ele vira string única. Voltar na aula 09, 29:31.

#Curso - em - V í  d  e  o  -  P  y  t  h  o  n
#01234 5 67 8 9 10 11 12 13 14 15 16 17 18 19 20

#Prática

#frase = 'Curso em Vídeo Python'
#print(frase[3]) #Resposta: s

#frase = 'Curso em Vídeo Python'
#print(frase[3:13]) #Resposta: so em Víde

#frase = 'Curso em Vídeo Python'
#print(frase[:13]) #Resposta: Curso em Víde

#frase = 'Curso em Vídeo Python'
#print(frase[1:15]) #Resposta: urso em Vídeo

#frase = 'Curso em Vídeo Python'
#print(frase[1:15:2]) #Resposta: urso em Vídeo

#frase = 'Curso em Vídeo Python'
#print(frase[1::2]) # Aqui significa q não sei qual é o final, mas ele vai até o final da string, de 2 em 2. Resposta: us mVdoPto

#frase = 'Curso em Vídeo Python'
#print(frase[::2]) #Aqui eu não sei o início, nem o final. Ele vai de 2 em 2. Resposta: Croe íe yhn

#Qdo quiser imprimir um texto longo, fazer dessa forma:
#print("""Welcome! Asdijsaidjsaidjis sadsaijiewiw aisdigjw!""")
#Colocar print, parenteses e 3 aspas no começo e no final.

#frase = 'Curso em Vídeo Python'
#print(frase.count('o')) #Resposta: 3

#frase = 'Curso em Vídeo Python'
#print(frase.count('O')) #Resposta: 0 pq não tem nenhuma letra O maiúscula, e ele busca exatamente o que vc pedir.

#frase = 'Curso em Vídeo Python'
#print(frase.upper().count('O') #Resposta: 3 pq vc está jogando para letra maiúscula.

#frase = 'Curso em Vídeo Python'
#print(len(frase.strip())) #R: 21 len verifica o tamanho da frase, então são 21 letras, e o strip remove os espaços indesejados.

#frase = 'Curso em Vídeo Python'
#print(frase.replace('Python', 'Android')) #R: Curso em Vídeo Android

#frase = 'Curso em Vídeo Python'
#print(frase[0]) #R: C

#frase = 'Curso em Vídeo Python'
#frase[0] = 'J' #R: Vai dar erro, pq é imutável

#frase = 'Curso em Vídeo Python'
#frase.replace('Python', 'Android')
#print(frase)
#R: Curso em Vídeo Python pq vc não pediu p/ salvar os resultados, para isso
#seria necessário utilizar uma função de transformação de string (frase.replace( , )), e faça uma atribuição ( frase = frase.replace('Python', 'Android')

#frase = 'Curso em Vídeo Python'
#print('Curso' in frase) #R: True pq Curso está dentro da frase

#frase = 'Curso em Vídeo Python'
#print(frase.find('Curso')) #R: 0 , significa q Curso está na posição zero.

#frase = 'Curso em Vídeo Python'
#print(frase.find('Vídeo')) #R: 9 , significa q Vídeo começa na letra 9

#frase = 'Curso em Vídeo Python'
#print(frase.find('video')) #R: -1 pq não tem a palavra video em minúsculo nem sem acento.

#frase = 'Curso em Vídeo Python'
#print(frase.lower().find('vídeo')) #R: 9. pq aqui estamos transformando em minúsculo para encontrar a palavra vídeo, e ela começa na posição 9.

#frase = 'Curso em Vídeo Python'
#print(frase.split()) #R:['Curso', 'em', 'Vídeo', 'Python']

#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[0]) #R Curso, pq aqui ele vai pegar o primeiro item da lista.

#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[2] [3]) #R e, pq vc está pedindo pra ele pegar o dividido 2 que é (Vídeo) e mostre a letra 3, que é a letra e.

#Exercícios

#022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quatas letras tem o primeiro nome

#nome = input('Digite seu nome: ').strip()
#print('Analisando seu nome...')
#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {}'.format(len(nome) - nome.count('')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#num = int(input('Digite um número: '))
#n = str(num)
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

#maneira matemática

#num  = int(input('Digite um número: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(u))
#print('Dezena: {}'.format(d))
#print('Centena: {}'.format(c))
#print('Milhar: {}'.format(m))

#024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
#Exercício q todo mundo tentou, mas não conseguiram fazer de forma completa.

#cid = str(input('Em que cidade você nasceu? ')).strip() #strip para retirar os espaços
#print(cid[:5].upper() == 'SANTO') #aqui o .upper jogou tudo pra maiúscula, então independente do q for digitado, se for essa palavra ele vai identificar.
                                  #o [:5] os dois pontos é pq vai pegar do início da palavra e vai até o 5, já q o Python só vai até o 4

#025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#nome = str(input('Digite seu nome completo: ')).strip()
#print('Seu nome tem Silva? {}'.format(nome[0:].upper() = = 'SILVA')) #eu q fiz

#Outra maneira de fazer a busca por nome no começo da STRING:
# nome = str(input('Qual é o seu nome completo? ')).strip()
#print('Seu nome tem Silva? {}'.format(nome[:5] == 'Silva')) #Guanabara

#nome = str(input('Qual é o seu nome completo? ')).strip()
#print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) #in não é um método, é um operador do Python

#026 - Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

#frase = str(input('Digite uma frase: ')).upper().strip()
#print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
#print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
#print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #rfind procure a partir do lado direito. Ele vai achar a última posição.
#frase: A filha da Xuxa se chama Sasha, ela tem uma casa com chão sujo, pois a sasha fez xixi no chão da sala

#027 -  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# - Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

#n = str(input('Digite seu nome: ')).strip()
#nome = n.split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1])) # No len eu vou saber quantas posições tem o nome.

#Como colocar as cores
#from termcolor import colored
#print(colored('Lições de Python', 'pink'))




