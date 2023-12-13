#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m2.
# Ex: Qual é a altura dessa parede?
# Ex: Qual é a largura dessa parede?
# Ex: Qual é a área dessa parede?

# Sabendo que cada litro de tinta pinta 2 m2, quantos litros de tinta eu vou precisar para pintar essa parede toda?

# Meu código:

#altura = float(input('Qual é a altura dessa parede? '))
#largura = float(input('Qual é a largura dessa parede? '))
#area = altura * largura
#tinta = area / 2
#print ('Para pintar uma parede de {} metros, vou precisar de {} litros de tinta'.format(area, tinta))

#Jeito que o Guanabara fez:

larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))