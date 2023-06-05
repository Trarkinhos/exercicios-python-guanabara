# Escreva um programa que converta uma temperatura digitada
# em ºC e converta para ºF.
# Exemplo: 25ºC para Fahrenheit é 77ºF: 

# Code:
celsius = int(input('Insira a temperatura em Celsius: '))
print('{}ºC para Fahrenheit é: {}ºF'
      .format(celsius, ((celsius / 5) * 9) + 32))
