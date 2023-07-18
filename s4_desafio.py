print('Exercício de fixação 8: Crie um programa que solicite o nome de quatro times de futebol e '
      'simule partidas de forma que cada time jogue uma vez com os outros três. Na partida, '
      'deve perguntar quantos gols fez cada time e somar as devidas pontuações. '
      'Ao final, deve dizer quais times foram campeões, uma vez que pode haver empate em pontuação. '
      'Observação: vitória vale 3 pontos para o vencedor, '
      'empate vale 1 ponto para cada time e derrota não soma pontos.')

times = []
tabela = [[], [], [], []]
for c in range(0, 4):
      n = str(input('Digite o nome de um time de futebol: ')).title()
      times.append(n)

for j in range(1, 4):
      for i in range (0, 5):
            print(f'Jogo: {times[i]} x {times[j]}')
            gols0 = int(input(f'Gols do {times[i]}: '))
            gols1 = int(input(f'Gols do {times[i+1]}: '))
            if gols0 > gols1:
                  tabela[i].append(3)
            elif gols0 == gols1:
                  tabela[i].append(1)
                  tabela[j].append(1)
            else:
                  tabela[j].append(3)

print(f'Jogo: {times[1]} x {times[2]}')
print(f'Jogo: {times[1]} x {times[3]}')
print(f'Jogo: {times[2]} x {times[3]}')
print(tabela)
