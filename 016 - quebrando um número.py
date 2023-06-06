# Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela sua porção inteira.
# Exemplo: O número 6.127 tem a parte inteira 6.

# Code:
from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')
