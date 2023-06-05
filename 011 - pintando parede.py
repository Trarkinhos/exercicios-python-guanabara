# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a quantidade de tinta necessária para pintá-la,
# Sabendo que cada litro de tinta, pinta uma área de 2m².
# Exemplo: Para 40m, será necessário {}l de tinta para pintar a parede.

# Code
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print('Para {}m, será necessário {}l de tinta para pintar a parede'
      .format((largura * altura), ((largura * altura)/2)))
