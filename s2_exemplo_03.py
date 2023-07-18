ano_atual = 2022
ano_nascimento = int(input('Qual ano você nasceu? '))
aniversario = str(input('Já fez aniersário esse ano? ')).upper()
if aniversario == 'SIM':
    idade =  ano_atual - ano_nascimento
else:
    idade =  ano_atual - ano_nascimento - 1
print(f'Sua idade é {idade}')
