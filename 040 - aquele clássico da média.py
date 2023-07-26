# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
# uma mensagem no final de acordo com a média atingida:

# - Média abaxio de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Code:
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

if (((n1 + n2) / 2) < 5):
    print('REPROVADO')
elif (((n1 + n2) / 2) >= 5 and ((n1 + n2) / 2) < 6.9):
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
