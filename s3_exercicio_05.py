print('''Exercício de fixação 5: Crie um programa que peça dois números ao usuário – o primeiro será o numerador e o segundo, o expoente. A saída do programa deve ser o resultado da operação: numerador elevado ao expoente. Observação: não usar função interna que calcula automaticamente potência.''')

numerador = int(input('Digite o númerador: '))
expoente = int(input('Digite o expoente '))
total = 1
for c in range(1, expoente + 1):
    total *= numerador
print(total)