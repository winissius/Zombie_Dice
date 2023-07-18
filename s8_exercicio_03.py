import random


class Baralho:
    __valores = ["1", "2", "3", "4", "5", "6", "7", "7", "9", "10", "dama", "valete", "rei"]
    __naipes = ["ouros", "espadas", "copas", "paus"]
    __cartas = []

    def __init__(self):
        self.__criar_baralho()
        self.__embaralhar()

    def __criar_baralho(self):
        for valor in range(len(self.__valores)):
            for naipe in range(len(self.__naipes)):
                self.__cartas.append(self.__valores[valor] + " de " + self.__naipes[naipe])
        self.__cartas.append("** Coringa **")
        self.__cartas.append("** Coringa **")

    def __embaralhar(self):
        for i in range(1000):
            pos1 = random.randint(0, 53)
            pos2 = random.randint(0, 53)
            aux = self.__cartas[pos1]
            self.__cartas[pos1] = self.__cartas[pos2]
            self.__cartas[pos2] = aux

    def sortear(self):
        if len(self.__cartas) == 0:
            return "Acabaram as cartas"
        else:
            return self.__cartas.pop()


if __name__ == '__main__':
    baralho = Baralho()
    for i in range(57):
        print(baralho.sortear())