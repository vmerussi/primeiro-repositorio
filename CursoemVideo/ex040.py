# Desafio 040
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira + segunda) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(primeira, segunda, media))
if media < 5.0:
    print('O aluno está REPROVADO.')
elif 5.0 <= media < 7.0:
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7.0:
    print('O aluno está APROVADO.')

    