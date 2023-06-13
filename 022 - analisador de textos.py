# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas e minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

# Code:
nome = str(input('Digite seu nome completo: '))
print(f"""
    - O nome com todas as letras maiúsculas: {nome.strip().upper()}
    - O nome com todas as letras minúsculas: {nome.strip().lower()}
    - Quantas letras ao todo (sem considerar espaços): {len(''.join(nome.strip().split()))}
    - Quantas letras tem o primeiro nome: {len(nome.strip().split()[0])} 
""")
