print('Exercício de fixação 9: Crie um programa que simule um carrinho de compras, solicitando o '
      'nome do produto (não pode ser vazio), seu valor (valor decimal, positivo) e quantidade a ser comprada '
      '(valor inteiro, positivo). Ao incluir um produto, deve perguntar se o usuário deseja fechar o pedido ou '
      'incluir mais produtos. Todos os dados devem ser validados. Ao final da compra, '
      'deve ser informado o valor total do pedido.')

continuar = 'k'
compra = 0
while True:
    if continuar == 'N':
        break
    while True:
        try:
            nomeProduto = input('Qual o nome do produto? ')
            if nomeProduto == '':
                print('Por favor digite o nome do produto')
            else:
                break
        except:
            print('Nome do produto inválido')
    while True:
        try:
            valorProduto = float(input('Qual o valor do produto?: '))
            break
        except:
            print('Digite um valor válido')
    while True:
        try:
            qtdProduto = int(input('Quantidade de produto'))
            if qtdProduto >= 1:
                break
            else:
                print('Quantidade inválida')
        except:
            print('Quantidade inválida')
    continuar = str(input(('Deseja continuar? [S/N]'))).upper()
    compra += valorProduto * qtdProduto
print(f'O valor total da compra é R$ {compra:.2f}')