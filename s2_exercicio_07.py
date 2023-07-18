l1 = int(input('Primeiro lado do triângulo '))
l2 = int(input('Segundo lado do triângulo '))
l3 = int(input('Terceiro lado do triângulo '))
if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1+l2): # verificação se é triangulo, caso um dos and for negativo, tudo é falso
    print('É Triângulo', end=' ')
    if l1 == l2 == l3:
        print('Do tipo Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Do tipo Isoceles')
    else:
        print('Do tipo Escaleno')
else:
    print('Não é triângulo')
