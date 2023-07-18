'''Exercício de fixação 2: Crie uma classe de cartas de baralho com o nome de Carta.
Ao imprimir a carta, deve ser mostrada uma carta de 1 a 10 ou figuras
(dama, valete ou rei) e um naipe (ouros, espadas, copas ou paus).'''

import random

class Carta:
    naipe = ('Copas', 'Paus', 'Ouros', 'Espadas')
    numero = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei')
    cartas = []
    def __init__(self):
        self.__criar_baralho()

    def __criar_baralho(self):
        pass

    def imprimir(self):
        pass



if __name__ == '__main__':
    carta = Carta()
    carta.imprimir()
    for i in range(5):
        carta.imprimir()