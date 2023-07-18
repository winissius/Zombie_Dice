print('Exercício de fixação 2: Crie um programa que cadastre os funcionários de uma empresa e seus dependentes. '
      'O funcionário deve ser cadastrado com matrícula, nome e dependentes.'
      ' Os dependentes devem ser inseridos dinamicamente em uma tupla. Dica: use o operador “+=”.')
cadastro = []
dep = " "
dependentes = ()
while True:
    nome = str(input('Nome: '))
    matricula = int(input('Matricula: '))
    while dep != "0":
        dep = str(input('Digite o nome do dependente (0 para sair)'))
        if dep != "0":
            dependentes += (dep, )
    funcionario = (nome, matricula, dependentes)
    cadastro.append(funcionario)
    if dep == "0":
        break
print(cadastro)