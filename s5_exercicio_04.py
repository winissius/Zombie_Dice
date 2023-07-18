print('Exercício de fixação 4: Crie um programa que efetue o cadastro de produtos e preços. '
      'Caso o produto já exista, deve perguntar se o usuário pretende atualizar o valor. '
      'Imprima o dicionário no fim do programa em formato de lista.')
compra = {}
while True:
      nome = str(input('Digite o nome do produto: '))
      valor = float(input('Digite o valor do produto: '))
      if nome in compra:
            r = str(input(f'Deseja atualizar o valor do item? Já existe um valor de R$ {compra[nome]} para esse item: ')).lower()
            if r == 's':
                compra[nome] = valor
            else:
                  print('Okay, não alterado')
      compra[nome] = valor
      continuar = str(input('Cadastrar um novo produto? (s/n)')).lower()
      if continuar == "n":
            break

for k, v in compra.items():
      print(f'{k} = {v}')