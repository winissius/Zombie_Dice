print('Exercício de fixação 8: Crie um programa que gere a série de Fibonacci enquanto o valor for menor que um valor '
      'informado pelo usuário. Observação: série de Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55, ... '
      'é formada por 0, 1 e, partir deste ponto, sempre será a soma dos dois valores anteriores.')

n = int(input('Digite o valor limite de Fibonnaci deseja ver: '))
c = 0
t1 = 0
t2 = 1
f = 0
print('0 1', end=' ')
while True:
      t3 = t1 + t2
      if n < t3:
            break
      print(t3, end=' ')
      t1 = t2
      t2 = t3
      c += 1

