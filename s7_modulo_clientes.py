"""
Módulo de cadastro de clientes
"""


def editar_cliente(nome, clientes):
    pesquisa = pesquisar_cliente(nome, clientes)
    if pesquisa[1]:
        cpf = input(f"Digite o novo CPF de {nome}: ")
        clientes[nome] = cpf
        return True
    else:
        return False


def inserir_cliente(clientes):
    cliente = solicitar_dados_cliente()
    pesquisa = pesquisar_cliente(cliente[0], clientes)
    if pesquisa[1]:
        if cliente[1] == pesquisa[0]:
            return False
    clientes[cliente[0]] = cliente[1]
    return True


def listar_clientes(clientes):
    print("*** Lista de Clientes ***")
    for cliente in clientes:
        print(f"{clientes[cliente]:>12}: {cliente}")
    print("*** Fim da Listagem ***")


def menu():
    print("*** CLIENTES ***")
    print("1. Inserir cliente")
    print("2. Editar cliente")
    print("3. Listar clientes")
    print("4. Pesquisar cliente")
    print("5. Sair")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 5:
        return op
    else:
        print("Opção inválida.")


def pesquisar_cliente(nome, clientes):
    if nome in clientes:
        return clientes[nome], True
    else:
        return "", False


def solicitar_dados_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    return nome, cpf


def inicio_clientes(clientes: dict):
    while True:
        op = menu()
        if op == 1:
            if inserir_cliente(clientes):
                print("Cliente cadastrado com sucesso")
            else:
                print("Operação falhou")
        elif op == 2:
            nome = input("Digite o nome do cliente a ser editado: ")
            if editar_cliente(nome, clientes):
                print("Cliente editado com sucesso")
            else:
                print("Operação falhou")
        elif op == 3:
            listar_clientes(clientes)
        elif op == 4:
            nome = input("Digite o nome do cliente a ser editado: ")
            pesquisa = pesquisar_cliente(nome, clientes)
            if pesquisa[1]:
                print("*** Dados do Cliente Pesquisado ***")
                print(f"{pesquisa[0]:>12}: {nome}")
            else:
                print("Operação falhou")
        else:
            break


if __name__ == '__main__':
    clientes_local = {}
    inicio_clientes(clientes_local)


