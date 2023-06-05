# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar.
# Exemplo: R$100 convertido para dolar: 20,31 (cotação 05/06/23: 4,92)

# Code:
real = float(input('Quanto de dinheiro você tem: R$'))
print('R${} convertido para dolar: {:.2f} (cotação 05/06/23: 4,92)'
      .format(real, (real / 4.92)))
print('R${} convertido para euro: {:.2f} (cotação 05/06/23: 5,27)'
      .format(real, (real / 5.27)))
