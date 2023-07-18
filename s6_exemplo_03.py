print('Exemplo de aplicação 3: Elabore um programa que use uma função chamada somar(), '
      'que efetua a soma de uma quantidade aleatória de números informados, retornando o resultado da operação.')
def somar(*n):
    s = 0
    for i in range(len(n)):
        s += n[i]
    print(s)

somar(2, 3, 4, 5, 8)
