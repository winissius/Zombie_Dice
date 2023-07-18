def separador_numeros(*num):
    pares = []
    impares = []
    for n in num:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        soma = sum(pares) + sum(impares)
    return pares, impares, soma




numeros = separador_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'A soma é {numeros[2]}\n'
      f'A lista de pares é {numeros[0]}\n'
      f'A lista de impares é {numeros[1]}')

