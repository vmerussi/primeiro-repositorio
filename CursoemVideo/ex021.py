#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#Dica: Dá para fazer com módulos. Qual módulo vc vai carregar, como vc vai carregar, tenta fazer.

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#Toda vez que for baixar a música em MP3, colocar input igual como está na última linha.
