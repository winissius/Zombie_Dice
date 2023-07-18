print('Exercício de fixação 3: Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes, removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos.')

s = str(input('Digite algo:'))
consoantes =''
for l in s:
    if l not in 'aiou':
        consoantes += l
    else:
        consoantes += ''
print(consoantes)
