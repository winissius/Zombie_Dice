print('Exercício de fixação 7:Dado o vetor nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], '
      'crie uma matriz 3x3 com os três maiores elementos na primeira linha, '
      'os três elementos intermediários na segunda linha e os elementos menores na terceira linha')

nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
sort = sorted(nums)
maiores = []
intermediarios = []
menores = []
for c in range(0, 3):
      menores.append(sort[c])
      maiores.append(sort[(6+c)])
      intermediarios.append(sort[3+c])
print(maiores)
print(intermediarios)
print(menores)
