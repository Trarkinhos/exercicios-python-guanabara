# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# R$7,00 por cada Km acima do limite.

# Code:
km = float(input('Qual é a velocidade atual do carro? '))

if(km > 80):
    print('Você estava acima da velocidade permitida (80km), terá que pagar uma multa de R${:.2f}!'.format((km-80)*7))

print('Bom dia, dirija com segurança!')
