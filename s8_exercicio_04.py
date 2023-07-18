'''
Exercício de fixação 4:

Crie uma classe Carro com as seguintes funcionalidades:

- Um veículo tem certo consumo de combustível (medido em km/l) e certa quantidade de combustível no tanque.
- O consumo é especificado no construtor e o nível de combustível inicial é 0.
- Forneça um método abastecer(), que abasteça o carro com o valor passado de litros de combustível.
- Forneça um método andar(), que simule o ato de dirigir o veículo por certa distância,
    reduzindo o nível de combustível no tanque de gasolina.
- Forneça um método nivel_combustivel(), que retorne o nível atual de combustível.
'''

class Carro:
    def __init__(self, consumo):
        self.__consumo = consumo
        self.__nivel = 0

    def abastecer(self, litros):
        self.litros = litros
        self.__nivel += litros
        return self.__nivel

    def andar(self, distancia):
        self.distancia = distancia
        gasto_combustivel = self.distancia / self.__consumo
        self.__nivel -= gasto_combustivel
        if self.__nivel <= 0:
            print('Carro sem combustível')
        else:
            return self.__nivel

    def nivel_combustivel(self):
        print(f'O carro ainda tem {self.__nivel:.2f} L')




if __name__ == '__main__':
    carro = Carro(12)
    carro.abastecer(100)
    carro.andar(1000)
    carro.nivel_combustivel()
    carro.andar(300)