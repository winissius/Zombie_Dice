turno = str(input('Qual turno você trabalha: M - Manhã, T - Tarde, N - Noite: ')).upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'T':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Entrada inválida')