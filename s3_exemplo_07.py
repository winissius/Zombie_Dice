print('Uso do CONTINUE')

mult = 1

for c in range(1, 11):
    n = int(input(f'Digite o {c}o número: '))
    if n == 0:
        continue
    mult *= n
print(mult)