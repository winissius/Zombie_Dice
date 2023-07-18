print('Exercício de fixação 1: Crie um programa que solicite ao usuário seis números, calculando a média, '
      'e mostre uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média')

boletim = []

for n in range(1, 7):
      notas = float(input(f'Digite a nota {n}: '))
      boletim.append(notas)
media = sum(boletim)/len(boletim)
acima = []
abaixo = []
for n in boletim:
      if n >= media:
            acima.append(n)
      else:
            abaixo.append(n)
print(f'A méida foi {media}\n'
      f'As notas acima da média são {acima}\n'
      f'As notas abaixo da média são {abaixo}')
