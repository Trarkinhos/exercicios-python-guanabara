# Faça um programa que leia um número inteiro qualquer e mostre na tela
# a sua tabuada.
# Exemplo: 10x1 = 10 | 10x2 = 20 | 10x3 = 30

# Code:
n = int(input('Digite um número para ver sua tabuada: '))
print('='*12)
print(' {}x{:2} = {} \n {}x{:2} = {} \n {}x{:2} = {} \n {}x{:2} = {} \n {}x{:2} = {}'
      .format(n, 1, (n*1), n, 2, (n*2), n, 3, (n*3), n, 4, (n*4), n, 5, (n*5)))
print('='*12)
print(' {}x{:2} = {} \n {}x{:2} = {} \n {}x{:2} = {} \n {}x{:2} = {} \n {}x{} = {}'
      .format(n, 6, (n*6), n, 7, (n*7), n, 8, (n*8), n, 9, (n*9), n, 10, (n*10)))
print('='*12)
