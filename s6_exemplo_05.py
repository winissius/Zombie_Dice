print('Exemplo de aplicação 5: Elabore um programa que, aplicando a fórmula de Bhaskara por funções, '
      'encontre as raízes de um polinômio do segundo grau, a saber:')

def delta(a, b, c):
    return b**2 - 4*a*c


def bhaskara(a, b, c):
      positivo = (-b + delta(a, b, c)**(1/2))/(2*a)
      negativo = (-b - delta(a, b, c)**(1/2))/(2*a)
      return positivo, negativo

resultado1 = bhaskara(1, 3, 1)
print(f'raiz positiva {resultado1[0]} '
      f'raiz negativa {resultado1[1]}')

resultado2 = bhaskara(1, 2, 1)
print(f'raiz positiva {resultado2[0]} '
      f'raiz negativa {resultado2[1]}')


resultado3 = bhaskara(1, 1, 1)
print(f'raiz positiva {resultado2[0]} '
      f'raiz negativa {resultado2[1]}')
