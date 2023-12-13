#Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exercer 30% do salário ou então o empréstimo será negado.

valorDaCasa = float(input('Valor da Casa: R$ '))
salarioComprador = float(input('Salário do comprador R$: '))
anosAPagar = int(input('Quantos anos de financiamento? '))
valorParcelas = valorDaCasa / (anosAPagar * 12)
valorPermitido = salarioComprador * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}.'.format(valorDaCasa, anosAPagar, valorParcelas))
if valorParcelas <= valorPermitido:
    print('APROVADO!)
else:
    print('EMPRÉSTIMO NEGADO! Sua renda é menor que o percentual estipulado!')
