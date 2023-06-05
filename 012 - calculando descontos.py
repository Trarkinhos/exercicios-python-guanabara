# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
# Exemplo: O valor do produto de R$100 com 5% de desconto é: R$95

# Code:
produto = float(input('Digite o valor do produto: R$'))
print('O valor do produto de R${:.2f} com 5% de desconto é: R${:.2f}'
      .format(produto, (produto - (produto * 0.05))))
