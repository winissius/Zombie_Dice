'''
Exercício de fixação 5:

Crie uma classe Bomba que simule uma bomba de combustíveis de um posto. A bomba pode injetar dois tipos de combustível:
 gasolina ou álcool,
 podendo definir no construtor da classe a quantidade e o valor do litro de cada um.
 Deve possuir os seguintes métodos:
 abastecer_valor(valor, tipo_combustivel), que mostra quantos litros foram colocados no veículo.
abastecer_litros(litros, tipo_combustivel), que mostra o valor no abastecimento.
fechar(), que mostra ao final do dia quanto foi ganho no valor total da bomba e quanto sobrou de cada tipo de combustível.
'''

class Bomba:
    def __init__(self, quantidade_gasolina, quantidade_alcool, valor_gasolina, valor_alcool):
        self.quantidade_gasolina = quantidade_gasolina
        self.quantidade_alcool = quantidade_alcool
        self.valor_gasolina = valor_gasolina
        self.valor_alcool = valor_alcool
        self.lucro = 0

    def abastecer_valor(self, valor, tipo_combustivel):
        if tipo_combustivel == 'gasolina':
            litros = valor / self.valor_gasolina
            self.quantidade_gasolina -= litros
        else:
            litros = valor / self.valor_alcool
            self.quantidade_alcool -= litros
        self.lucro += valor

    def abastecer_litros(self, litros, tipo_combustivel):
        if tipo_combustivel == 'gasolina':
            self.quantidade_gasolina -= litros
            valor = self.valor_gasolina * litros
        else:
            self.quantidade_alcool -= litros
            valor = self.valor_alcool * litros
        self.lucro += valor

    def fechar(self):
        print(f'Quantidade de álcool restante: {self.quantidade_alcool:.2f} L')
        print(f'Quantidade de gasolina restante:{self.quantidade_gasolina:.2f}')
        print(f'Lucro total: R$ {self.lucro:.2f}')

if __name__ == '__main__':
    bomba = Bomba(100, 100, 4.3, 3.1)
    bomba.abastecer_valor(100, "gasolina")
    bomba.abastecer_valor(50, "alcool")
    bomba.abastecer_litros(30, "gasolina")
    bomba.abastecer_litros(70, "alcool")
    bomba.fechar()

