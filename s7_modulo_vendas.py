"""
Módulo de vendas
"""

import s7_modulo_clientes

from collections import namedtuple

Venda = namedtuple("Venda", ["valor", "cliente"])

def listar_vendas(vendas, clientes):
    print("*** Lista de Vendas ***")
    print("  código      vendas        cliente")
    for venda in vendas:
        print(f"{venda:^10} R${vendas[venda].valor:^14.2f} {vendas[venda].cliente} ({clientes[vendas[venda].cliente]})")
    print("*** Fim da Listagem ***")


def menu():
    print("*** SISTEMA ***")
    print("1. Registrar uma venda")
    print("2. Listar vendas")
    print("3. Gerenciar clientes")
    print("4. Sair")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 3:
        return op
    else:
        print("Opção inválida.")


def registrar_venda(vendas, clientes):
    codigo = int(input("Digite o número do pedido: "))
    nome = input("Digite o nome do cliente: ")
    valor = float(input("Digite o valor da venda: "))
    pesquisa = s7_modulo_clientes.pesquisar_cliente(nome, clientes)
    if pesquisa[1]:
        venda = Venda(valor=valor, cliente=nome)
        vendas = venda
        return True
    else:
        return False


def inicio_vendas(vendas: dict):
    while True:
        op = menu()
        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            s7_modulo_clientes.inicio_clientes(vendas["clientes"])
        else:
            break


if __name__ == '__main__':
    vendas_local = {}
    Vendas_local["vendas"] = {}
    vendas_local["clientes"] = {}
    inicio_vendas(vendas_local)

if __name__ == '__main__':
    vendas_local = {}
    vendas_local["clientes"] = {}
    inicio_vendas(vendas_local)