print('Fatorial 2.0')
numero = int(input('Digite um número: '))
fatorial = 1

for c in range(numero, 0, -1):
    fatorial *= c
    if c >=2:
        print(f'{c} x ', end='')
    else:
        print('1')
print(f'\nO fatorial de {numero} é {fatorial}')