print('Exercício de fixação 1: Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final essas informações.')

cpar = cimpar = 0

for c in range(1, 11):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cpar += 1
    else:
        cimpar += 1
print(f'Você digitou {cpar} números pares e {cimpar} números impares')