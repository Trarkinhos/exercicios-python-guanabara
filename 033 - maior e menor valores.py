# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Code:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor: '))

# verificação do menor
menor = a
if b<a and b<c:
    menor = b

if c<a and c<b:
    menor = c

print(f'O número com menor valor foi {menor}')

# verificação do maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O número com maior valor foi {maior}')
