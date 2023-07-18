print('Exercício de fixação 3: Crie um programa que receba uma lista de números e retorne a média.')

def media(*l):
    soma = 0
    for n in l:
        soma +=n
    m = soma/len(l)
    print(m)



media(2, 5, 9, 4, 11)
