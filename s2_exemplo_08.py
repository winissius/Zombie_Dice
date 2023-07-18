print('Digite 3 números dfierentes')
n1 = int(input('Primeiro número '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 < n2:
    if n1 < n3:
        print(f'O primeiro número {n1} é o menor')
    else:
        print(f'O terceiro número {n3} é o menor')
if n2 < n1:
    if n2 < n3:
        print(f'O segundo número {n2} é o menor')
    else:
        print(f'O terceiro número {n3} é o menor')
