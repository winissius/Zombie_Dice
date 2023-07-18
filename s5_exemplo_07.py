print('Exemplo de aplicação 7: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda. '
      'Caso seja informado um nome já existente, deve perguntar se deseja alterar os dados existentes. '
      'Caso seja um telefone já existente, deve informar que esse telefone já está cadastrado em outro contato, '
      'não podendo ser efetuada a inclusão. Ao final, deve exibir o dicionário.')

agenda = {}

while True:
    contato = str(input('Qual o nome do contato? '))
    telefone= str(input('Qual o telefone do contato? '))
    if telefone in agenda.values():
        print('Esse telefone já está cadastrado, não podemos alterar.')
    elif contato in agenda.keys():
        alterar = str(input(f'Deseja alterar os dados existesntes? [S/N], esse contato já tinha o telefone {agenda[contato]}')).upper()
        if alterar == 'S':
            agenda[contato] = telefone
        else:
            print('Okay, não alterado')
    else:
        agenda[contato] = telefone
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == "N":
        break
print(agenda)