# Desafio 039
# Faça um programa que leia o ano de nascimento de uma jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.

'''from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))'''

from datetime import date
atual = date.today().year
nascimento = int(input('\033[34mAno de Nascimento: \033[m'))
print('''Escolha seu sexo:  
[F] Feminino 
[M] Masculino''')
opcao = input('Sua opção: ')
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if opcao == 'F':
    print('Você do sexo Feminino não precisa fazer o alistamento obrigatório!'.format(opcao, 'F'))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

