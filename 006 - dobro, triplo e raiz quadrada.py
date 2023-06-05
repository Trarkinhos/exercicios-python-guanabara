# Crie um algoritmo que leia um número e mostre o seu dobro, triplo
# e raiz quadrada.
# Exemplo: Número informado: 25 | Dobro: 50 | Triplo: 75 | Raiz quadrada: 5

# Code:
n = int(input('Digite um número: '))
print('Número informado: {} | Dobro: {} | Triplo: {} | Raiz quadrada: {}'.format(n, (n * 2), (n * 3), (n ** (1/2))))
