print('''A matriz-identidade é uma matriz com a mesma quantidade de linhas e colunas, 
apresentando todos os elementos da diagonal principal (de cima para baixo, da esquerda para a direita) iguais a 1 e 
os demais elementos iguais a 0. 
Crie um programa que solicite o tamanho da matriz desejada, gerando a matriz-identidade
''')

tamanho = int(input('Qual o tamanhod a matriz identidade que deseja: '))
identidade = []
for c in range (tamanho):
    for i in range(tamanho):
        identidade.append([])
        for j in range(tamanho):
            if i == j:
                identidade[i].append(1)
            else:
                identidade[i].append(0)
    for linha in identidade:
        print(linha)