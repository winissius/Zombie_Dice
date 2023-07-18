print('Exemplo de aplicação 2: Elabore um programa que solicite ao usuário cinco números e exiba duas listas, '
      'uma de números pares e outra de números ímpares.')

impar = []
par = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Os pares são: {par}\n'
      f'os impares são: {impar}')
