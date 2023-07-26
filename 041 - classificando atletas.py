# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM | Até 14 anos: INFATIL | Até 19 anos: JUNIOR | até 20 anos: SÊNIOR | Acima: MASTER

# Code:
from datetime import date

idade = date.today().year - int(input('Digite seu ano de nascimento: '))

if (idade <= 9):
    print(f'Você tem {idade} anos e faz parte da categoria: MIRIM')
elif (idade <= 14):
    print(f'Você tem {idade} anos e faz parte da categoria: INFATIL')
elif(idade <= 19):
    print(f'Você tem {idade} anos e faz parte da categoria: JÚNIOR')
elif (idade <= 25):
    print(f'Você tem {idade} anos e faz parte da categoria: SÊNIOR')
elif (idade > 25):
    print(f'Você tem {idade} anos e faz parte da categoria: MASTER')
    

