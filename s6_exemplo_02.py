def inserir (nome, telefone, agenda):
      if nome in agenda:
           alterar = str(input(f'Deseja alterar o telefone do contato?'))
           if alterar == 's':
                 return True
           else:
                 print('Telefone já cadastrado, o usuário optou por não alterar')
                 return False
agenda1 = {}
r = 's'
while r != 'n':
      n = str(input('Nome: '))
      t = str(input('Telefone: '))
      if inserir(n, t, agenda1):
            print('telefone alterado com sucesso')
            agenda1[n] = t
      elif False:
            print('usuário optou por não alterar')
      else:
            print('cadastrado com sucesso')
            agenda1[n] = t
      r = str(input('Continuar [S/N]')).lower()
print(agenda1)
