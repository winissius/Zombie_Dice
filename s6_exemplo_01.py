print('Exemplo de aplicação 1: Elabore um programa que cadastre contatos de uma agenda telefônica. '
      'A função de cadastro deve ser realizada dentro de uma função chamada inserir, '
      'que recebe como parâmetros o nome e o telefone do contato, bem como a agenda de contatos.')

agenda = {}
r = 's'

def cadastrar():
     nome = input('Nome: ')
     telefone = int(input('Telefone: '))
     agenda[nome] = telefone


while r != 'n':
      cadastrar()
      r = str(input('Deseja continuar [S/N]')).lower()
print(agenda)
