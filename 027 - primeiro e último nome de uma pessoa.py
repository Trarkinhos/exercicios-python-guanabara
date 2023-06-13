# Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# > primeiro = Ana
# > último = Souza

# Code:
nome = str(input('Digite seu nome completo: ')).strip().upper()
print(f"""
    Seu nome: {nome}
    Primeiro nome: {nome.split()[0]}
    Último nome: {nome.split()[-1]}
""")
