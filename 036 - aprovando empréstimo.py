# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.

# - Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
# - do salário ou então o empréstimo será negado.

# Code:

print('== ANÁLISE DE EMPRESTIMO ==')

valor_casa = float(input('| Digite o valor da casa: R$'))
salario_mensal = float(input('| Digite o seu salário mensal: R$'))
anos_pagando = int(input('| Digite em quantos anos deseja pagar: '))

print('> O parcelamento da casa em {} anos ficou de R${:.2f}/mensal'
      .format(anos_pagando, (valor_casa / (anos_pagando *12))))

if ((valor_casa / (anos_pagando *12)) > (salario_mensal * 0.3)):
    print('STATUS:\033[1;31;40m EMPRÉSTIMO NEGADO \033[m')
else:
    print('STATUS:\033[1;32;40m EMPRÉSTIMO APROVADO \033[m')
