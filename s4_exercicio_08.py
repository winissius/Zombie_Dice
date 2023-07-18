print('Exemplo de aplicação 8: Dada a matriz m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], '
      'efetue a soma de todos os seus elementos e exiba o resultado.')

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0

for n in m:
    for c in n:
        soma += c
print(soma)