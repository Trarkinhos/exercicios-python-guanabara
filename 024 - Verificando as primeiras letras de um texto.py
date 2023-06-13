# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com o nome "Santo".

# Code:
cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()
print(f'A cidade começa com a palavra "Santo"? {"SANTO" in cidade.split()[0]}')
