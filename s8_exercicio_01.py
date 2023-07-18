'''Exercício de fixação 1: Crie uma classe Televisor, em que o usuário é capaz de trocar de canais
e aumentar/diminuir o volume.
O limite de canais válidos vai de 1 a 15 e o limite de volume válido vai de 0 a 10.
No caso de um canal inválido, deve ser definido como padrão o canal 1.'''

class Televisor:
    def __init__(self):
        self.__canal = 1
        self.__volume = 0

    def trocar_canal(self, canal):
        if 1 <= canal <= 15:
            self.__canal = canal
        else:
            self.__canal = 1
        print(f'Volume = {self.__volume} Canal = {self.__canal}')

    def aumentar_volume(self):
        if 10 > self.__volume >= 0:
            self.__volume = self.__volume + 1
        print(f'Volume = {self.__volume} Canal = {self.__canal}')

    def diminuir_volume(self):
        if 10 >= self.__volume > 0:
            self.__volume = self.__volume - 1
        print(f'Volume = {self.__volume} Canal = {self.__canal}')


if __name__ == '__main__':
    televisor = Televisor()
    televisor.trocar_canal(5)
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.trocar_canal(1)
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.aumentar_volume()
    televisor.trocar_canal(20)
    televisor.diminuir_volume()
    televisor.diminuir_volume()
    televisor.diminuir_volume()
