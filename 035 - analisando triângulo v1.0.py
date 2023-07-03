# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

# Code:
print('==( Digite 3 comprimentos )==')
a = int(input('1º comprimento: '))
b = int(input('2º comprimento: '))
c = int(input('3º comprimento: '))

if (a==b) and (a==c) and (b==c):
    print('Isso é um triângulo')

else:
    print('Isso não é um triângulo')
