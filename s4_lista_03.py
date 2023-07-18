print('Exercício de fixação 3: Crie um programa que leia as temperaturas médias de cada mês do ano '
      'e as armazene em uma lista; use outro vetor para guardar e exibir, quando necessário, '
      'o nome dos meses do ano; calcule a média anual de temperatura e '
      'informe quais meses ficaram acima da média anual.'
      '')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []
soma = 0
for m in meses:
      temp = int(input(f'Digite a temepratura de {m}: '))
      temperatura.append([m, temp])

for m in temperatura:
      soma += m[1]
media = soma/len(temperatura)

print(f'Os meses que tiveram temperatura superior a {media} de  oC foram:')
for m in temperatura:
      if m[1] > media:
            print(f'{m[0]}: {m[1]} graus')