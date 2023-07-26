# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# 1 - para binário | 2 - para octal | 3 - para hexadecimal

# Code:

num = int(input('Digite um número inteiro: '))
base = int(input('Escolha: 1 - binário | 2 - octal | 3 - hexadecimal: '))

if base == 1:
    print(f'O número {num} convertido para binário: {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num} convertido para octal: {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} convertido para hexadecimal: {hex(num)[2:]}')
else:
    print(f'Não existe opção {base} para ser convertido')
