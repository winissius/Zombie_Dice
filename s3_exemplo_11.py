print('Validação de erros')

while True:
    try:
        n = float(input('Digite um número decimal: '))
        break
    except ValueError:
        print('valor inválido')
print(f'Número validado: {n}')