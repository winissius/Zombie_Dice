print('Exemplo de aplicação 6: Solicite ao usuário que digite três coordenadas (x, y), '
      'armazenando-as em uma matriz bidimensional.')

coordenadas = []

for c in range (1, 4):
      x = int(input('Digite uma coordenada para x:'))
      y = int(input('Digite uma coordenada para y:'))
      coordenadas.append([x, y]) #insere uma matriz dentro da matriz coordenadas
print(coordenadas)