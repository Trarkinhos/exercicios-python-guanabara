# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
# dígitos separados.
# Exemplo: Seu número 1234 | Unidade: 4 | Dezena: 3 | Centena: 2 | Milhar: 1

# Code:
num = int(input('Digite um número de 0 até 9999: '))
print(f"""
    Número informado: {num}
    - Unidade: {num // 1 % 10}
    - Dezena: {num // 10 % 10}
    - Centena: {num // 100 % 10}
    - Milhar: {num // 1000 % 10}
""")
