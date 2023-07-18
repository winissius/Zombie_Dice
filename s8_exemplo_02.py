'''Exemplo de aplicação 2: Elabore uma classe que simule um dado de jogo. No construtor,
deve-se informar quantas faces possui o dado. Caso o valor informado seja inválido,
o dado será padrão, de seis faces. Deve ter um método privado de calcular a jogada
e um método público de retorno do valor do dado para o usuário.
Ao final, deve testar a classe e todos os seus métodos.'''

from random import randint

class RollDice:
    def __init__(self, faces = 6):
        self.faces = faces if faces % 2 == 0 and faces > 0 else 6

    def __roll(self):
        return randint(1, self.faces)

    def face(self):
        return self.__roll()

    def dice(self):
        print(f'O dado escolhido é o de {self.faces} faces')


dado20 = RollDice(20)
dado20.dice()
print(f'Você rolou {dado20.face()}')

dado20 = RollDice(12)
dado20.dice()
print(f'Você rolou {dado20.face()}')

