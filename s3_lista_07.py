matriz = [[4, 2, 3], [5, 1, 0]]
i = len(matriz[0])
j = len(matriz[1])
menor = maior = matriz[0][0]
for k in range(0, i):
    if menor > matriz[0][k]:
        menor = matriz[0][k]
    if maior < matriz[0][k]:
        maior = matriz[0][k]
    if menor > matriz[1][k]:
        menor = matriz[1][k]
    if maior < matriz[1][k]:
        maior = matriz[1][k]
print(f'Maior = {maior}\n'
      f'Menor = {menor}\n')
