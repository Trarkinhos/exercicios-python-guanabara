# Faça um programa que ielai um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.
# Exemplo: Seno: 0.71 | Cosseno: 0.71 | Tangente: 1.00

# Code:
from math import radians, sin, cos, tan

angulo = radians(float(input('Digite o ângulo: ')))
print("Seno: {:.2f} | Cosseno: {:.2f} | Tangente {:.2f}"
      .format(sin(angulo), cos(angulo), tan(angulo)))
