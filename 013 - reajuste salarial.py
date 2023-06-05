# Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário, com 15% de aumento.
# Exemplo: Parabéns! seu salário de R$1500 teve um aumento de 15%, você passou a ganhar R$1725

# Code:
salario = float(input('Digite o seu salário atual: R$'))
print('Parabéns! seu salário de R${:.2f} teve um aumento de 15%, você passou a ganhar R${:.2f}!'
      .format(salario, (salario + (salario * 0.15))))
