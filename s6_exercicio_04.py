def fatorial(n: int):
    '''

    :param n: número informado na chamada da função para cálculo do fatorial
    :return:valor do resultado do fatorial
    '''
    fat = 1 #garante que o fatorial de 0 é 1, segudno definição matemática
    for c in range(n, 1, -1):
        fat *= c
    return fat

print(fatorial(5))