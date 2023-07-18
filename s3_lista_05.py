notas = []
t = 3 #tamanho da classe
c_aprovados = c_reprovados = 0
soma = 0
for c in range(0, t):
    n = float(input('Nota '))
    notas.append(n)
    if n >= 7:
        c_aprovados += 1
    else:
        c_reprovados += 1
for n in notas:
    soma += n
media = soma/len(notas)
print(f'A média da classe é {media:.2f}\n'
      f'O número de aprovados é {c_aprovados}\n'
      f'O número de reprovados é {c_reprovados}')