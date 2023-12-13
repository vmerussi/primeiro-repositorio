#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))
m = (n1 + n2) / 2
#print('A média entre {} e {} é igual a {}'.format(n1, n2, m))

#Ou para diminuir 1 dígito no resultado, o print fica assim:

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))