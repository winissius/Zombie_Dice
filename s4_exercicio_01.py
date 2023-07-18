print('Exemplo de aplicação 1: Elabore um programa que solicite ao usuário cinco números, '
      'armazene-os em uma lista e exiba como resultado os dados obtidos.')

num = [0, 0, 0, 0, 0]
#num = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    num[c] = n
    #num.append(n)
print(num)