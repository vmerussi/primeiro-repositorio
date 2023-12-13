# Aula 013 - Estrutura de Repetição For.
# Laços, Repetições ou Iterações
# Laço de Repetição é uma estrutura de repetição mais simples. Depois vamos para as mais complexas.
# Laço é a mesma coisa que FOR, e Intervalo = range

# Como escrever em Python:

# laço c no intervalo(1,10)                      |  for c in range(1,10):
#   passo        #(comando)                      |    passo (note q a identação está mais para dentro
# pega                                           |  pega (comando pega está fora do laço pq não está na mesma identação de passo, então ele não faz parte do laço.

# Laço com variável de controle (1, 10)

# laço c no intervalo(0,3)
# for c in range(0,3)
# se tiver moeda     if coin:
# passo                pega
# pula                  passo
# passo                    pula
# pega                       passo
# pega

#for c in range(0, 50, 10):
#    print(c)
#print('FIM')

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))


# for c in range(0,6):
#  print('Oi')
# print('FIM') #se esse print FIM estiver à esquerda, ou fora do for, ele vai repetir Oi 6x e FIM uma vez.
# se estiver dentro do for, como o exemplo acima, ele entra no laço e repete 6x Oi e FIM.#
 
# Nesse caso Oi e FIM ficam dentro do for, então eles aparecem 6x.
# Se mudar a identação do fim para a esquerda, aparecerá 6x Oi e FIM 1 vez.

# Para pular de 2 em 2.

# for c in range(0, 7, 2):
#    print(c)
#    print('FIM')

# Crie vários exemplos para não errar na identação dessas estruturas.

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')

#for c in range(1,10):
#    passo
#pega #( se pega estivesse começando na mesma linha do passo ele estaria dentro do laço, mas como não está, ele está fora do laço. Lembrar sempre da identação )

#for c in range(0,3): #colocar uma estrutura dentro da outra, como vimos anteriormente, chama-se aninhar.
#    if moeda
#        pega
#    passo
#    pula
#passo
#pega

#for c in range(1, 6): # de (1,6) ele considera de 1 a 5 e, o 6 ele desconsidera. E vai escrever Oi 5x e no final a palavra FIM.
#    print('Oi')
#print('FIM')

#for c in range(0, 6): #Se for de 0,6, ao executar ele vai mostrar 6x, pq ele começa do zero 0.
#    print('Oi')
#    print('FIM') #aqui o fim está dentro do for, portanto executará Oi e FIM 6x cada. Cuidado com a identação, pq ela dá rasteira nas pessoas.
                #se colocar o fim fora do for, ou seja, para a esquerda, ele executará uma única vez.

#for c in range(0, 6): #ele vai contar de 0 até 5, pq o último ele ignora.
#    print(c)
#print('FIM')

#for c in range(1,7): #ele vai contar de 1 até 6. Colocamos 1 número a mais para contar até 6.
#    print(c)
#print('FIM')

#for c in range(6, 0, -1): #Para contar de 6 até 0, ou seja, contar para trás, vc vai colocar vírgula e -1. Vai aparecer 6,5,4,3,2,1, FIM.
#    print(c)
#print('FIM')

#for c in range(0, 7, 2): #Aqui ele vai contar de 0 até 7 pulando de 2 em 2. Resultado: 0, 2, 4, 6, FIM.
#    print(c)
#print('FIM')

#n = int(input('Digite um número: '))
#for c in range(0, n):
#    print(c)
#print('FIM')

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')

#i = int(input('Início: '))
#f = int(input('FIM:'))
#p = int(input('Passo:'))
#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

#Inicio: 2, Fim: 9, Passo: 3
#Ele começa no 2 vai até o nove pulando de 3 em 3.
#Resultado: 2, 5, 8 (pq 2 + 3 = 5 + 3 = 8)

#Inicio: 1, Fim: 100, Passo: 10
#Ele começa no 1 vai até o 100 pulando de 10 em 10.
#Resultado: 1, 11, 21, 31, 41, 51, 61, 71, 81, 91, FIM. (pq 1 + 10 = 11 + 10 = 21)

#for c in range(0, 3): #Nesse caso ele vai pedir 3 vezes por número. Se colocar 10 no lugar do 3 ele vai pedir 10 vezes um número.
#    n = int(input('Digite um valor: '))
#print('fim')

#s = 0
#for c in range(0, 4):
#    n = int(input('Digite um valor: '))
#    s += n # ou  s = s + n
#print('O somatório de todos os valores foi {}'.format(s))

#Desafio 46
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#Desafio 47
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#Desafio 48
#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#Desafio 49
#Refaça o DESAFIO 009(tabuada), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#Desafio 50
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#Desafio 51
#Desenvolva um programa que leia o primeiro termo de uma PA(progressão aritimética). No final, mostre os 10 primeiros termos dessa progressão.
#Ex: começa no 1 termina no 100 pulando de 10 em 10. Isso é progressão aritimética.

#Desafio 52
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. ( Número primo é aquele divisível por 1 ou por ele mesmo. Nenhum número
#no intervalo ele será divisível).

#Desafio 53
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Palíndromo é uma frase q vc pode ler de trás pra frente e de frente para trás que será a mesma coisa. Ex: APOS A SOPA. A SACADA DA CASA, A TORRE DA DERROTA,
#O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#Desafio 54 ( maioridade só com 21 anos)
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#Desafio 55
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#Desafio 56
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#-A média de idade do grupo
#-Qual é o nome do homem mais velho
#-Quntas mulheres têm menos de 20 anos.




