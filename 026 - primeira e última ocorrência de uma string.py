# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A"
# > Em que posição ela aparece a primeira vez
# > Em que posição ela aparece a última vez

# Code:
frase = str(input('Digite um texto: ')).strip().upper()
print(f"""
    - Quantas vezes a letra A apareceu: {frase.count('A')}
    - Posição que ela apareceu a primeira vez: {frase.find('A')+1}
    - Posição que ela apareceu a última vez: {frase.rfind('A')+1}
""")
