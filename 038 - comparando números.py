# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# O primeiro valor é maior | O segundo valor é maior | Não existe valor maior, os dois são iguais

# Code:

primeiro = float(input('Primeiro número: '))
segundo = float(input('Segundo número: '))

if(primeiro > segundo):
    print('O primeiro valor é maior')
elif(segundo > primeiro):
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
