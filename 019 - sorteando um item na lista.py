# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.
# Exemplo: O aluno que vai apagar o quadro é: Marcos

# Code:
from random import choice

primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do quarto aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))

print(f'O aluno que vai apagar o quadro é: {choice([primeiro, segundo, terceiro, quarto])}')
