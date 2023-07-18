print('''
Exercício de fixação 6: Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações. Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".''')

media = soma = contador = 0

while True:
    n = int(input('Digite um número '))
    if n == 0:
        break
    else:
        soma += n
        contador += 1
        media = soma / contador
if contador == 0:
    print('Não foram informados números')
else:
    print(f'A média é {media}')
