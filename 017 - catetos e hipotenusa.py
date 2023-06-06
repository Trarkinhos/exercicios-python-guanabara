# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Exemplo: A hipotenusa de 7 e 5: 8.60

# Code:
from math import hypot

y = float(input('Digite o comprimento do cateto oposto: '))
x = float(input('Digite o comprimento do cateto adjacente: '))
print('A hipotenusa de {} e {}: {:.2f}'.format(x, y, hypot(x, y)))
