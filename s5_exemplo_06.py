print('Exemplo de aplicação 6: Elabore um programa que simule o cadastro de telefones '
      'com dicionário como uma agenda, exibindo, ao final, o dicionário.')

agenda = {}

while True:
    contato = str(input('Qual o nome do contato? '))
    telefone= str(input('Qual o telefone do contato? '))
    agenda[contato] = telefone
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == "N":
        break
print(agenda)