#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#import time

#t = 10

#[print(t := t - 1) or time.sleep(1) for _ in range(t)] Esse é um método encontrado no Youtube.

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')

