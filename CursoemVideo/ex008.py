#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#medida = float(input('Digite um valor em metros: '))
#cm = medida * 100
#mm = medida * 1000
#print('O valor {} metros em centímetros é {}, e milímetros {}'.format(medida, cm, mm))

# Se não quiser nenhuma casa decimal, pode colocar {:0f}, ex:
#print('O valor {} metros em centímetros é {:.0f}, e milímetros {:.0f}'.format(medida, cm, mm))

#Continuação do desafio: você vai continuar lendo em metros, e mostre a quantidade de kilometros km, hectometros hm, decametros dam, decimetros dm, centimetros cc e milimetros mm.
m = float(input('Digite um valor em metros: '))
km = float(m/1000)
hm = float(m/100)
dam = float(m/10)
dm = float(m*10)
cm = float(m*100)
mm = float(m*1000)
print('A conversão da medida {}m para outras medidas de comprimento ficou em:'.format(m))
print('KM {}, HM {}, DAM {}, DM {}, CM {}, MM {:.0f}'.format(km, hm, dam, dm, cm, mm))



#Outro exemplo:

#valor = float(input('Digite uma distância em metros: '))
#print('A medida de {}m corresponde a\n'
     # '{:.3f}km (quilômetro)\n'
     # '{:.2f}hm (hectômetro)\n'
     # '{:.1f}dam (decâmetro)\n'
     # '{:.0f}dm (decímetro)\n'
     # '{:.0f}cm (centímetro)\n'
     # '{:.0f}mm (milímetro)'.format(valor,valor * 0.001,valor * 0.01, valor * 0.1, valor * 10, valor * 100, valor * 1000))


# Mais um exemplo:

#n = float(input('Uma distancia em metros:'))
#print(f'A medida de {n}m corresponde a\n{n/1000}km\n{n/100}hm\n{n/10}dam\n{n}m\n{n*10}dm\n{n*100}cm\n{n*1000}mm')

