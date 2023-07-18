s = int(input(('Informe o valor do saque:')))
n100 = n50 = n10 = n5 = n1 = r = s1 = s2 = s3 = s4 = 0
if 600 > s > 100:
    if 600 > s:
        n100 = s // 100
        s1 = n100 * 100
        r = s - s1
    if 100 > r:
        n50 = r // 50
        s2 = n50 * 50
        r = r - s2
    if 50 > r:
        n10 = r // 10
        s3 = n10 * 10
        r = r - s3
    if 10 > r:
        n5 = r // 5
        s4 = n5 * 5
        r = r - s4
    if 5 > r:
        n1 = r // 1
    print(f'Notas de 100: {n100}\n'
          f'Notas de 50: {n50}\n'
          f'Notas de 10: {n10}\n'
          f'Notas de 5: {n5}\n'
          f'Notas de 1: {n1}')
else:
    print('Valor inválido')



