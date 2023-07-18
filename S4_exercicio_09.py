print('Exemplo de aplicação 9: Em uma competição de saltos ornamentais, são obtidas dos jurados sete notas, '
      'sendo eliminadas a maior e a menor. A valoração do salto é feita pela soma das demais notas. '
      'Crie um programa que receba as notas dos juízes, remova a maior e menor nota e some as demais, '
      'fazendo uso de métodos de listas e funções built in.')

notas = []

for c in range(1, 8):
    n = int(input(f'Digite a nota {c}: '))
    notas.append(n)
notas2 = sorted(notas)
notas2.pop()
notas2.reverse()
notas2.pop()
print(f'A pontuação final do salto foi {sum(notas2)}')