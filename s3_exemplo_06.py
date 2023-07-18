print('Uso do break')

soma = 0
for c in range(1, 4):
    n = int(input((f'Digite o {c}o número: ')))
    soma += n
    if n == 0:
        break
print(f'A soma é {soma}')