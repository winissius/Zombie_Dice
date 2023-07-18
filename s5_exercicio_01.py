print('Exercício de fixação 1: Crie um programa que efetue o cadastro de pessoas com nome, '
      'RG e CPF por meio de tuplas, adicionando-as a uma lista e imprimindo essa lista no fim do programa.')
cadastro = []
while True:
    nome = str(input('Nome: '))
    RG = int(input('RG: '))
    CPF = int(input('CPF: '))
    dados = (nome, RG, CPF)
    cadastro.append(dados)
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == "N":
        break
print(cadastro)