print('Digite o valor que deseja sacar')
valor = int(input())
if valor > 600 or valor < 100:
    print('Valor inválido')
else:
    if valor >= 100:
        n100 = valor // 100
        resto = valor % 100
    if valor >= 50:
        n50 = resto // 50
        resto = resto % 50
    if valor >= 10:
        n10 = resto // 10
        resto = resto % 10
    if valor >= 5:
        n5 = resto // 5
        resto = resto % 5
    if valor >= 1:
        n1 = resto // 1
    print(f'Notas de 100: {n100}')
    print(f'Notas de 50: {n50}')
    print(f'Notas de 10: {n10}')
    print(f'Notas de 5: {n5}')
    print(f'Notas de 1: {n1}')
