print('Exercício de fixação 2: Crie um programa que solicite ao usuário duas listas com cinco elementos cada e,'
      ' como resultado, crie uma terceira lista que intercale os elementos das anteriores.')

n1 = [1, 3, 5, 7, 9]
n2 = [2, 4, 6, 8, 10]
n3 = []
for n in range(len(n1)):
      n3.append(n1[n])
      n3.append(n2[n])
print(n3)

