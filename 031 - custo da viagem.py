# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

# Code:
km = float(input('Qual a distância da sua viagem? '))

if (km > 200):
    print('A passagem para viagem de {}km fica no valor de R${:.2f}'
          .format(km, (km * 0.45)))
else:
    print('A passagem para viagem de {}km fica no valor de R${:.2f}'
          .format(km, (km * 0.50)))
