# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
# Exemplo: A ordem de apresentação será: Marcos, João, Pedro, Guilherme.

# Code:
from random import shuffle

primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do quarto aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))

lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista)

print(f'A ordem de apresentação será: {lista}.')
