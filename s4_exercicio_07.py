print('Exemplo de aplicação 7: Solicite ao usuário que entre com diversos nomes, '
      'informando de forma separada nome e último sobrenome. '
      'Ao final, mostre uma lista de nomes no formato: sobrenome, nome. '
      'Para encerrar a entrada de dados, basta o usuário inserir no nome o texto “sair”.')

pessoas = []

while True:
    nome = str(input('Digite o nome:'))
    if nome == 'sair':
        break
    sobrenome = str(input('Digite o sobrenome: '))
    pessoas.append([sobrenome, nome])

for p in pessoas:
    for nomes in range(len(p) - 1):
        print(f'{p[nomes]}, {p[nomes + 1]}')

print(''
      'OUTRA SOLUÇÃO'
      '')
nomes = []
while True:
    nome = input("Digite o nome: ")
    if nome == "sair":
        break
    sobrenome = input("Digite o sobrenome: ")
    nome_completo = [nome, sobrenome]
    nomes.append(nome_completo)

for nome in nomes:
    print(nome[1] + ", " + nome[0])

