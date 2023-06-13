# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva"
# no nome.

# Code:
nome = str(input('Digite seu nome completo: ')).upper().strip()
print(f'Você não possui "Silva" no nome: {"SILVA" in nome.split()}')
