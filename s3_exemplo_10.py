print('Validação de erros')

while True:
    try:
        n = int(input('Digite um número inteiro: '))
        print(f'Número validado: {n}')
        break
    except ValueError:
        print('valor inválido')

