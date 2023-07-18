print('Exercício de fixação 1: Crie um programa que calcule, a partir de uma função,'
      ' o fatorial de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.')

def fatorial(n):
    fat = 1
    for c in range(n, 1, -1):
        fat *= c
    print (fat)

fatorial(5)