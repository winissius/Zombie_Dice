print('Digite suas 4 notas bimestrais:')
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
print('Informe o número de faltas:')
faltas = int(input())
m = (n1 + n2 + n3 + n4) / 4
aprov = ((1-(faltas/40)) * 100)
print(f'Sua média é {m} e sua frequência {aprov}')
if m >= 7 and aprov == True:
    print('Aprovado pro nota e frequência')
elif m >= 7 and aprov < 75:
    print('Reprovado por frequência')
elif m <= 7 and aprov >= 75:
    print('Reprovado por nota')
else:
    print('Reprovado por nota e frequência')