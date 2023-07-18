salario = float(input('Qual seu salário? '))
if salario >= 5000:
    print(f'Seu abono de fim de ano será R$ {salario * 0.1:.2f}')
else:
    print(f'Seu abono de fim de ano será R$ {salario * 0.15:.2f}')