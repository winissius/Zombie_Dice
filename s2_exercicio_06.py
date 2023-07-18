n1 = float(input('Digite o primeiro número '))
n2 = float(input('Digite o segundo número: '))
op = str(input('Digite + - / *: '))
r = 0
if op == '+':
    r = n1 + n2
elif op == '-':
    r = n1 - n2
elif op == '/':
    r = n1 / n2
elif op == '*':
    r = n1 * n2
else:
    op = 'Erro'
if op == 'erro':
    print('Opção inválida')
else:
    print(f'{n1} {op} {n2} = {r}')
    print(n1,op,n2,'=',r)
