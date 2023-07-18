# Classe Cliente

class Cliente:
    nome = "João"
    cpf = "123.456.789-00"

    def imprimir(self):
        print(f"Cliente:", self.nome, "- CPF:", self.cpf)


cliente = Cliente()
cliente.imprimir()


class Cliente:

    def __init__(self, nome1, cpf1):
        self.__nome = nome1
        self.__cpf = cpf1

    def alterar_dados(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def imprimir(self):
        print(f"Cliente:", self.__nome, "- CPF:", self.__cpf)

cliente = Cliente('Winissius', '06824716901')

cliente.imprimir()'''

'''print(cliente.nome) #impossivel devido ao escopo'''

from revisao_classe_com_modulos import Cliente

c = Cliente()
c.imprimir()