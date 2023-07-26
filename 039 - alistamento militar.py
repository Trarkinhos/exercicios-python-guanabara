# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:

# - se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - se já passou do tempo do alistamento

# Code:
from datetime import date

idade = date.today().year - int(input("Em que ano você nasceu? "))

if idade == 18:
    print(f'Você tem {idade} anos, chegou a hora de se alistar.')
elif idade < 18:
    print(f'Você tem {idade} anos, você ainda vai se alistar.')
    print(f'Seu alistamento deve ser feito daqui a {18 - idade} anos.')
else:
    print(f'Você tem {idade} anos, já passou o tempo de se alistar.')
    print(f'Seu alistamento deveria ser feito a {idade - 18} anos atrás.')
