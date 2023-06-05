# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros.
# Exemplo: 50 metros para centímetros | 50 metros para milímetros

# Code:
metros = float(input('Digite a quantidade de metros a serem convertidos: '))
print('{} metros para centímetros: {}cm | {} metros para milímetros {}mm'
      .format(metros,(metros * 100), metros, (metros * 1000)))
