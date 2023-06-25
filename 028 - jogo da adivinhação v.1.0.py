# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Code:
from random import randint

number_computer = randint(0, 5)

print('-=-'*20)
print('Estou pensando em um número de 0 à 5, tente adivinhar')
print('-=-'*20)

number_player = int(input('Tente adivinhar o número que estou pensando: '))

if (number_player == number_computer):
    print('Parabéns! você adivinho o número que estava pensando!')
else:
    print('Você errou! tente novamente!')
