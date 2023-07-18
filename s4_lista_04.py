print('Exercício de fixação 4: Crie um programa que efetue a soma de duas matrizes 3x3,'
      ' sabendo que a soma desse tipo de matriz é uma nova matriz 3x3, '
      'sendo cada elemento resultado da soma dos elementos das matrizes na mesma posição.')

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[3, 2, 3], [1, 3, 3], [0, 2, 2]]
m3 = [[], [], []]
m4 = []
for n in range(len(m1)):
      for c in range(3):
            m3[n].append(m1[n][c]+m2[n][c])
for n in m3:
      print(n)
