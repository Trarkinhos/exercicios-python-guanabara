# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele.
# Exemplo: Tipo primitivo? Str | Só tem espaços? | É um número?

# Code:
x = input('Digite alguma coisa: ')
print(' Tipo primitivo? {} \n Só tem espaços? {} \n É um número? {} \n É alfabético? {} \n É alfanúmerico? {} \n Está em maiúsculas? {} \n Está em minúsculas? {} \n Está capitalizada? {}'
      .format(type(x), x.isspace(), x.isnumeric(), x.isalpha(), x.isalnum(), x.isupper(), x.islower(), x.istitle()))
