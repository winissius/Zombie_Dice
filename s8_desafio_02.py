from datetime import date

class Carro:
    def __init__(self, modelo, marca, ano, combustivel, quilometragem):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__combustivel = combustivel
        self.__quilometragem = quilometragem

    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getCombustivel(self):
        return self.__combustivel

    def setCombustivel(self, combustivel):
        self.__combustivel = combustivel

    def consultarIsencaoIPVA(self):
        data_atual = date.today()
        ano_atual = int(date.today().year)
        idadeVeiculo = ano_atual - self.__ano
        if idadeVeiculo > 20:
            print('Isento de IPVA')
        elif idadeVeiculo == 20:
            print('Isento de IPVA no próximo ano')
        else:
            print(f'Será isento de ipva em {20 - idadeVeiculo}')

    def getQuilometragem(self):
        return self.__quilometragem

    def setQuilometragem(self, quilometragem):
        self.__quilometragem = quilometragem


carro1 = Carro('Fusca', 'Volkswagen', 1956, 'Gasolina', 0)
print(carro1.getModelo())
carro1.consultarIsencaoIPVA()

print('')
carro2 = Carro('Polo', 'Volkswagen', 2019, 'Flex', 1000)
print(carro2.getModelo())
carro2.consultarIsencaoIPVA()
print('Quilometragem:', (carro2.getQuilometragem()))
carro2.setQuilometragem(2000)
print('Quilometragem:', (carro2.getQuilometragem()))