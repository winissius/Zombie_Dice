print('Digite suas 4 notas: ')
nota1 = float(input('Digite a sua nota 01: '))
nota2 = float(input('Digite a sua nota 02: '))
nota3 = float(input('Digite a sua nota 03: '))
nota4 = float(input('Digite a sua nota 04: '))
media = (nota1+nota2+nota3+nota4) / 4
print(f'Sua média na disciplina foi {media:.2f}')
if media >= 7:
    print(f'Você foi aprovado')
else:
    print(f'Você foi reprovado')