#Condições Aninhadas - Qdo vc vai encaixando as coisas. No Python vc pode pegar estruturas condicionais e colocar dentro de estruturas condicionais.
#Isso nós chamamos de Condições Aninhadas. Na outra aula apresentamos 2 caminhos, true e false, se o carro fosse para a esquerda (true), o outro caminho
#seria o false. Nesse caso além da esquerda, temos o caminho da direita e a outra possibilidade de caminho, um terceiro caminho, que é o caminho do meio.
#Como tem um caminho dentro de outro caminho, significa que é uma condição aninhada. Como na aula anterior, o siga e o pare vai acontecer todas as vezes.
#Sempre vai começar com if, nunca vai começar com elif, e nem sempre vai ter o else, o elif e o else são opcionais, até qdo vc usa elif o else é opcional.

'''carro.siga()                                                   carro.siga()
se carro.esquerda()                                            if carro.esquerda():
    carro.siga()                                                   carro.siga()
    carro.direita()                                                carro.direita()
    carro.siga()                                                   carro.siga()
    carro.direita()                                                carro.direita()
    carro.esquerda()                                               carro.esquerda()
    carro.siga()                                                   carro.siga()
    carro.direita()                                                carro.direita()
    carro.siga()                                                   carro.siga()
senão se carro.direita()                                       elif carro.direita() # elif é a junção de else com if
    carro.siga()                                                   carro.siga()
    carro.esquerda()                                               carro.esquerda()
    carro.siga()                                                   carro.siga()
    carro.esquerda()                                               carro.esquerda()
    carro.siga()                                                   carro.siga()
senão                                                          else:
    carro.siga()                                                  carro.siga()
carro.pare()                                                   carro.pare()'''


'''if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.ré():
    bloco 3
else:
    bloco4'''

#Essas são as estruturas padrão, de forma simplificada ( com 3 possibilidades ). Se tiver 4 possibilidades, é só acrescentar outro elif.
#Dentro de 1 if, vc pode usar vários elifs , Else pode usar nenhuma ou 1 vez.
#Vc pode ter 1 if sem else, e vários elifs;
#Vc pode ter 1 if, vários elifs e 1 else.
# Agora nunca pode usar um elif sem if

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo': #Condição simples                           #Estrutura condicional aninhada
    print('Que nome bonito!') #Condição Simples
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':       #Estrutura condicional aninhada
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':                       #Estrutura condicional aninhada
    print('Belo nome feminino')
else:                                                             #Estrutura condicional aninhada
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai pergunatr o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exercer 30% do salário ou então o empréstimo será negado.

# Desafio 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

# Desafio 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

# Desafio 039
# Faça um programa que leia o ano de nascimento de uma jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.

# Desafio 040
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Desafio 041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

# Desafio 042
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

# Desafio 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

# Desafio 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro / cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

# Desafio 045
# Crie um programa que faça o computador jogar Jokenpô com você.
