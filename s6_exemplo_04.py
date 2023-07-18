print('Exemplo de aplicação 4: Elabore um aplicativo que faça uso de uma função que receba diversos '
      'valores numéricos e retorne o maior e o menor valor da lista.')

def maior_menor(*lista):
      for i in range(len(lista)):
            maior = menor = lista[0]
            if lista[i] > maior:
                maior = lista[i]
            if lista[i] < menor:
                menor = lista[i]
      return maior, menor


resultado = maior_menor(7, 15, 3, 22, 1, 8)
print(resultado)
print(f'O maior é {resultado[0]} e o menor é {resultado[1]}')