print('Exemplo de aplicação 1: Elabore um programa que solicite ao usuário o cadastro de endereços '
      'para entrega de produtos de uma loja.')

print('Cadastro de Endereços de Entrega')
endereço = []
i = 0
while True:
      logradouro = str(input('Digite o logradouro: ')).title()
      numero = int(input('Digite o número: '))
      bairro = str(input('Digite o bairro: ')).title()
      cidade = str(input('Digite a cidade: ')).title()
      estado = str(input('Digite o estado: ')).upper()
      continuar = str(input('Deseja continuar? [S/N]')).upper()
      novo_endereço = (logradouro, numero, bairro, cidade, estado)
      endereço.append(novo_endereço)
      if continuar == 'N':
            break
print('Os endereços cadastrados são:')
for c in endereço:
      print(f'{i}. {c[0]}, {c[1]}, {c[2]}, {c[3]}/{c[4]} ')
      i += 1
