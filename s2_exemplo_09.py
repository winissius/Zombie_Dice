print('Digite 3 números diferentes')
n1 = int(input('Primeiro número '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 < n2 and n1 < n3:
    print('O primeiro é menor')
elif n2 < n1 and n2 < n3:
    print('O segundo é o menor')
else:
    print('O terceiro é o menor')