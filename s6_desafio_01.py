print('Exercício de fixação 6: Crie um programa que, fazendo uso de funções, '
      'cadastre contatos em uma agenda telefônica, podendo exclui-los. '
      'Deve ser exibido um menu com as opções: inserir, remover e sair.')

agenda = {}




def inserir(s):
    n = str(input('Nome do contato: '))
    t = str(input('Telefone do contato: '))
    agenda[n] = t

def excluir(s):
    n = str(input('Qual contato deseja remover: '))
    agenda.pop(n)

def menu():
    while True:
        print('MENU DA AGENDA')
        r = str(input('1 - Inserir\n'
                      '2 - Remover\n'
                      '3 - Sair\n'))
        if r == '1':
            inserir(r)

        elif r == '2':
            excluir(r)

        elif r == '3':
            break
    print('Obigado por utilizar a agenda WM')
    print(agenda)

menu()