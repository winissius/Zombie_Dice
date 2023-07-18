print('Exercício de fixação 2: Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles.')
menor = maior = 0
for c in range(1, 6):
    n = int(input(f'Digite o {c}o número: '))
    if c == 1:
        menor = maior = n
    if menor > n:
        menor = n
    if maior < n:
        maior = n
print(f'Dos 5 números digitados o maior é {maior} e o menor é {menor}')