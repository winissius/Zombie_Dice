print('ZOMBIE DICE- PROJETO DA DISCIPLINA - ALUNO: WINISSIUS MACHADO')

import random
from time import sleep
import operator

def inicializarDados(): #função que cria/inicializa os dados no tubo
    dado_verde = ('CPCTPC')
    dado_amarelo = ('TPCTPC')
    dado_vermelho = ('TPTCPT')
    # tubo de dados, onde fica armazenado os 13 dados
    tubo_dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
                  dado_verde, dado_amarelo, dado_amarelo, dado_amarelo,
                  dado_amarelo, dado_vermelho, dado_vermelho, dado_vermelho]
    return tubo_dados


def pegaDados(): #função que pega os dados do tubo
    while len(dados_sorteados) != 3:
        a = random.choice(tubo_dados)
        # adiciona ao copo de dados 3 dados aleatórios
        dados_sorteados.append(a)
        tubo_dados.remove(a)
        manter_dados_face()
    print(f'Ainda há {len(tubo_dados)} de dados')


def lancarDados(): #função que sorteia a face do dado
    print('\nRolando os dados:\n')
    for dados in dados_sorteados:
        #dentro o copo de dados escolhe uma face aleatória
        face = random.choice(dados)
        if face == 'C':
            print('Você rolou C e comeu um cérebro! Grrrr!')
            contador[0] += 1
        elif face == 'P':
            print('Você rolou P e sua vítima fugiu!')
            contador[1] += 1
            dadosface.append(dados)
        else:
            print('Você rolou T e tomou um tiro! ')
            contador[2] += 1


def manter_dados_face(): #função para re-rolar os dados que cairam face, se desejado
    if len(dadosface) < 3:
        for d in dadosface:
            dados_sorteados.pop()
            dados_sorteados.append(d)
            dadosface.pop(0)
    else:
        for d in dadosface:
            dados_sorteados.append(d)
            dados_sorteados.pop(0)

def minimo_de_jogadores(num, numero_jogadores):
    while numero_jogadores < num:
        numero_jogadores = int(input('Digite o número de jogadores: '))
        if numero_jogadores < num:
            print(f'AVISO: É necessário ao menos {num} jogadores')
    for c in range(0, numero_jogadores):  # adiciona a lista de jogadores
        nome_jogadores = str(input('Digite o nome do jogador: ')).title()
        jogadores.append(nome_jogadores)
    for j in jogadores:
        pontuação[j] = 0


def mostrarDados(): #função que exibe a cor do dado
    print('Dados sorteados adicionados ao copo:')  # apresenta os dados sorteados
    # modo de apresentar o nome dos dados sorteados
    for dados in dados_sorteados:
        if dados == 'CPCTPC':
            print('Dado verde')
        elif dados == 'TPCTPC':
            print('Dado amarelo')
        else:
            print('Dado vermelho')
    sleep(1)


def score(): #score TOTAL do jogo
    print('-=' * 25)
    print('\nPontuação TOTAL dos jogadores:\n')
    print('-=' * 25)
    sleep(2)
    for k, v in pontuação.items():
        print(f'Jogador {k} pontuação {v} Cérebros')


def turnosdejogo(): #função que exibe os turnos
    try:
        print('-=' * 25)
        print(f'Turno de {ordem_jogo[k]}') #nome dos jogadores com turno.
        print('-=' * 25)
    except:
        print('FIM DE JOGO!')


def scoreTurno(): #função contador do turno
    try:
        print(f'\nCONTADOR DESSE TURNO DO JOGADOR {ordem_jogo[k]}\n'
              f'Cérebros = {contador[0]}\n'
              f'Passos = {contador[1]}\n'
              f'Tiros = {contador[2]}') #placar por turno
    except :
        print()


def continuar_turno(continuar, contador, k, fim_de_turno):
    if contador[2] < 3:
        continuar = str(input('Deseja continuar? [S / N]')).upper()
        contador[1] = 0
    else:
        contador[0] = 0
    sleep(1)
    if continuar == 'N' or contador[2] >= 3:
        if contador[2] < 3:
            pontuação[ordem_jogo[k]] += contador[0]
        if k <= len(ordem_jogo):
            k += 1
        if k > len(ordem_jogo):
            k = 0
        contador = [0, 0, 0]
        dadosface = []
        print('\n====== FIM DO TURNO ======!\n')
        score()
    return fim_de_turno
    return k


def desempate(finalistas, ordem_jogo):
    ordem_jogo.clear()
    for j in finalistas.keys():
      ordem_jogo.append(j)
    return ordem_jogo


def champion(num, ordem_jogo, vencedor, contadormaiores):
    if k == len(ordem_jogo):
      for jogador, pontos in pontuação.items():
          maior = max(pontuação.values())
          if pontos >= maior:
              maior = pontos
          if pontos >= num:
                if pontos == maior:
                    contadormaiores += 1
      if contadormaiores == 1:
          vencedor = max(pontuação.items(), key=operator.itemgetter(1))[0]
          print(f'vencedor = {vencedor}')
      else:
          for jogador, pontos in pontuação.items():
            if pontos >= maior:
              finalistas[jogador] = pontos
              desempate(finalistas, ordem_jogo)
    return vencedor
    return ordem_jogo


jogadores = [] #lista dos jogadores
#definição inicial de número de jogadores para iniciar o laço
numero_jogadores = 0
continuar = 'k' #definição inicial de continuar para iniciar o loop
#definindo parametros iniciais como zero
k = 0
vencedor = ' '
fim_de_turno = False
finalistas = {}
contador = [0, 0, 0]
pontuação = {}
dadosface = []
contadormaiores = 0
minimo_de_jogadores(2, numero_jogadores)
tubo_dados = inicializarDados()
random.shuffle(jogadores)
ordem_jogo = jogadores


while vencedor == ' ':
    turnosdejogo()
    dados_sorteados = [] #copo de dados
    pegaDados()
    mostrarDados()
    lancarDados()
    sleep(1)
    scoreTurno()
    continuar_turno(continuar, contador, k, fim_de_turno)
    if len(tubo_dados) < 3:
        tubo_dados = inicializarDados()
    vencedor = champion(3, ordem_jogo, vencedor, contadormaiores)

print('\nFIM DO JOGO!')