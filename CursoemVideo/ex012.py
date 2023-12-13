# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#produto = float(input('Digite o valor do produto: '))
#desconto = produto * 0.05
#calculo = produto - desconto
#print('O preço final do produto com o desconto de 5% é R$:{}'.format(calculo))


# Jeito do Guanabara de resolver:

preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))