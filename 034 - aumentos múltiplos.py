# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salário superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

# Code:
salario = float(input('Digite seu salário atual: '))
    
if salario<=1250:
    print('Você teve um aumento de 15%, seu novo salário é de R${:.2f}'
          .format(salario + (salario * 0.15)))

else:
    print('Você teve um aumento de 10%, seu novo salário é de R${:.2f}'
          .format(salario + (salario * 0.10)))
