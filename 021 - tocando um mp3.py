# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Code:
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
