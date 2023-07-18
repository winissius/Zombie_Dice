print('Exercício de fixação 6: Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores '
      'sejam iguais, informar que os dados são inválidos e pedir novamente as informações. Caso contrário, exibir a'
      ' mensagem "Bem-vindo ao sistema!".')

login = senha = 1

while True:
    login = str(input('Digite seu login\n'))
    senha = str(input('Digite sua senha\n'))
    if login == senha:
          print('Dados inválidos')
    else:
          break
print('Bem vindo ao sistema!')