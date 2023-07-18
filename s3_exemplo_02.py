print('Fatorial')
n = int(input('Escolha um número: '))
fatorial = 1
for c in range(n, 1, -1):
    fatorial *= c
print(f'O fatorial de {n} é {fatorial}')