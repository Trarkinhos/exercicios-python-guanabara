# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
# e seu antecessor.
# Exemplo: Seu número: 10 | Antecessor: 9 | Sucessor: 11

# Code:
n = int(input('Digite um número: '))
print('Seu número: {} | Antecessor: {} | Sucessor: {}'.format(n, (n - 1), (n + 1)))
