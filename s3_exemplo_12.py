print('tratametno de erros')
print('Exemplo de aplicação 12: Elabore um programa que solicite um número inteiro ao usuário, em um intervalo entre 1 e 5.')

while True:
    try:
        n = int(input('Digite um número inteiro entre 1 e 5: '))
        if 5 >= n >= 1:
            break
    except ValueError:
        print('Valor inválido')
print(f'Valor validado: {n}')
