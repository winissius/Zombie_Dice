# aluno: Carlos Ryan da Rocha
# curso: Raciocínio Computacional
# atividade somativa 2
# zumbie dice
Dado = namedtuple('Dado', ['cor', 'faces'])


class ZombieDice:

    @staticmethod
    def lancar_dado(dado_lancado):
        """
            retorna o lado aleatoriamente do dado
            :param dado_lancado: Estrutura Dado que vai ser usada para ter uma face aleatória.
            :return: "C" or "T" or "P"
        """
        return choice(dado_lancado.faces)

    @staticmethod
    def gerar_tubo_embaralhado():
        """
            Gera um tubo com 13 dados embaralhados sendo 6 verdes, 4 amarelos e 3 vermelhos
            :return: List[Dado]
        """

        tubo = []

        # tipos de dados
        # letras: C = cérebro, T = tiro e P = passos
        dado_verde = Dado(cor='verde', faces=("C", "P", "C", "T", "P", "C"))
        dado_amarelo = Dado(cor='amarelo', faces=("T", "P", "C", "T", "P", "C"))
        dado_vermelho = Dado(cor='vermelho', faces=("T", "P", "T", "C", "P", "T"))

        # dados verdes ao tubo
        for _ in range(6):
            tubo.append(dado_verde)

        # dados amarelos ao tubo
        for _ in range(4):
            tubo.append(dado_amarelo)

        # dados vermelhos ao tubo
        for _ in range(3):
            tubo.append(dado_vermelho)

        # tubo com dados embaralhados
        return sample(tubo, len(tubo))

    @staticmethod
    def cadastrar_jogadore():
        """
             cadastro dos jogadores
            :return: { "nome_jogador": {"tiros": 0, "cerebros": 0, "passos": 0}, ... }
        """

        # quantia de jogadores
        numero_jogadores = int(input("Informe o número de jogadores: "))

        while numero_jogadores < 2:
            # Adverte o jogador e pede um novo valor
            print("\nZombie Dice deve ser jogado por pelo menos duas pessoas!")
            numero_jogadores = int(input("Informe o número de jogadores: "))

        # nome dos jogadores
        lista_jogadores = {}

        # pula uma linha
        print("")

        # nomes dos jogadores
        for i in range(0, numero_jogadores):
            novo_jogador = input(f"Digite no nome do jogador {i + 1}: ")

            while novo_jogador in lista_jogadores:
                print(f"Jogador {novo_jogador} já incluso anteriormente")
                novo_jogador = input(f"Digite um nome diferente de {novo_jogador} para o jogador {i + 1}: ")

            # score do jogador
            lista_jogadores[novo_jogador] = {"tiros": 0, "cerebros": 0, "passos": 0}

        # jogadores cadastrados
        return lista_jogadores

    @staticmethod
    def dados_no_copo(dados_tubo):
        """
        recebe os dados restantes no tubo e retorna os três dados selecionados para serem rolados
        :param dados_tubo: Dados presentes no tubo
        :return: List[Dado]
        """

        dados_copo = []

        # tira os 3 primeiros dados do tubo
        for _ in range(3):
            dados_copo.append(dados_tubo.pop(0))

        print(f"Dados no copo: {dados_copo[0].cor}, {dados_copo[1].cor}, {dados_copo[2].cor}\n")

        return dados_copo

    @staticmethod
    def lancar_dados_copo(self, jogador_turno, dados_copo, dados_tubo):
        """
            lança os três dados no existentes no copo, altera o score do jogador e retorna para o tubo
            os dados que tiveram valor 'passos'
            :param self: referência da classe
            :param jogador_turno: jogador atual
            :param dados_copo: três dados existentes no copo
            :param dados_tubo: dados restantes no copo
        """

        # joga os dados
        for dado in dados_copo:
            valor_dado = self.lancar_dado(dado)

            if valor_dado == "C":
                print(f"Dado {dado.cor} - Você capturou o humano e comeu um CÉREBRO!")
                jogador_turno["cerebros"] += 1
            elif valor_dado == "T":
                print(f"Dado {dado.cor} - O humano ATIROU em você! Cuidado para não morrer.")
                jogador_turno["tiros"] += 1
            else:
                print(f"Dado {dado.cor} - Os PASSOS do humano foram mais rápidos e ele fugiu! Vá atrás dele outra vez.")
                jogador_turno["passos"] += 1
                dados_tubo.append(dado)  # Devolve o dado para o tubo
                shuffle(dados_tubo)  # Embaralha o tubo outra vez

    @staticmethod
    def score_jogador(lista_jogadores, jogador_turno):
        """
            mostra a pontuação atual do jogador
            :param lista_jogadores: dicionário com os jogadores
            :param jogador_turno:  nome do jogador atual
        """

        print(f"\nA potuação de {jogador_turno} até agora é:")
        print(f"Cérebros comidos: {lista_jogadores[jogador_turno]['cerebros']}")
        print(f"Tiros recebidos: {lista_jogadores[jogador_turno]['tiros']}")
        print(f"Humanos que fugiram: {lista_jogadores[jogador_turno]['passos']}\n")

    @staticmethod
    def verifica_continuar_turno(self, lista_jogadores, jogador_turno):
        """
            Verifica se o jogador deseja continuar
            :param self: referência da classe
            :param lista_jogadores: lista com todos os jogadores
            :param jogador_turno: nome do jogador atual
            :return: True or False
        """

        self.score_jogador(lista_jogadores, jogador_turno)

        print("Quer continuar caçando humanos?")
        continuar_turno = input("Digite S para sim ou N para não: ")

        # confere se a resposta é válida
        while continuar_turno.lower() != "s" and continuar_turno.lower() != "n":
            print("\nResposta inválida!")
            continuar_turno = input("Digite S para sim ou N para não: ")

        if continuar_turno.lower() == "n":
            lista_jogadores[jogador_turno]["tiros"] = 0
            lista_jogadores[jogador_turno]["passos"] = 0

        return continuar_turno.lower() == "s"

    @staticmethod
    def verifica_vitoria(self, lista_jogadores, jogador_turno, numero_darrotados):
        """
            verifica se o jogador ganhou ou perdeu.
            :param self: referência da classe
            :param lista_jogadores: lista com todos os jogadores
            :param jogador_turno: nome do jogador que está na vez
            :param numero_darrotados: quantia de derrotados até o momento
            :return: {"vencedor": str, "contagem_derrotados": number, "continuar": boolean}
        """

        retorno = {"vencedor": '', "contagem_derrotados": numero_darrotados, "continuar": False}

        # reavalia condições de vitória ou derrota
        vitoria = lista_jogadores[jogador_turno]["cerebros"] >= 13
        derrota = lista_jogadores[jogador_turno]["tiros"] >= 3

        # valida condições para encerrar ou continuar
        if vitoria:
            print(f"\nVocê VENCEU! Os humanos nunca serão páreos para os zumbis!")
            retorno["vencedor"] = jogador_turno
        elif derrota:
            print("\nVocê PERDEU! Os cérebros dos humanos foram mais astutos dessa vez.")
            retorno["contagem_derrotados"] += 1
        else:
            retorno["continuar"] = self.verifica_continuar_turno(self, lista_jogadores, jogador_turno, )

        return retorno

    @staticmethod
    def verifica_jogar_novamente():
        """
            verifica se jogadores querem jogar novamente
            :return: True or False para resposta dos jogadores
        """

        # verifica se desejam jogar outra vez
        print("Quer caçar cérebros outra vez?")
        jogar_novamente = input("Digite S para sim ou N para não: ")

        # garante uma resposta válida
        while jogar_novamente.lower() != "s" and jogar_novamente.lower() != "n":
            print("\nResposta inválida!")
            jogar_novamente = input("Digite S para sim ou N para não: ")

        if jogar_novamente.lower() == "n":
            print("\nObrigado por jogar Zombie Dice!\n")
            return False
        else:
            print("\nE que uma nova caçada comece!\n")
            return True

    @staticmethod
    def jogar(self):
        """
            executa o jogo Zombie Dice
            :param self: referência da classe
        """

        print("Bem-vindos ao Zombie Dice! Estão preparados para caçar os humanos?")

        # cadastra os jogadores dessa partida
        jogadores = self.cadastrar_jogadore()
        quantia_jogadores = len(jogadores)

        # controle do loop de jogo
        vencedor = ''
        contagem_derrotados = 0

        while vencedor == '' and contagem_derrotados < quantia_jogadores - 1:
            # executa os turnos
            for jogador in jogadores:
                print()  # Pula uma linha para melhorar legibilidade das mensagens

                # caso haja vencedor, o jogo passa todos os turnos restantes e encerra
                if vencedor != '':
                    continue

                tubo_dados = self.gerar_tubo_embaralhado()  # inicia um novo tubo de dados

                # condições que permitem o jogador a continuar o turno ou não
                derrotado = jogadores[jogador]["tiros"] >= 3

                # caso seja uma nova rodada, passa o turno do jogador que perdeu em rodada anterior
                if derrotado:
                    print(f"{jogador} já foi derrotado. Passando turno para o próximo.\n")
                    continue

                # validação se é possível continuar o turno
                jogar = True

                print(f"{jogador} é o zumbi da vez!")
                print("Capture os humanos e coma seus cérebros!")

                # jogador continua enquanto desejar ou for possível
                while jogar:
                    # pula uma linha para melhorar separação das mensagens
                    print()

                    # armazena os dados desta jogada
                    dados_turno = self.dados_no_copo(tubo_dados)
                    self.lancar_dados_copo(self, jogadores[jogador], dados_turno, tubo_dados)

                    # valida o estado do jogador ou se ele deseja continuar jogando
                    estado_jogo = self.verifica_vitoria(self, jogadores, jogador, contagem_derrotados)

                    vencedor = estado_jogo["vencedor"]
                    contagem_derrotados = estado_jogo["contagem_derrotados"]
                    jogar = estado_jogo["continuar"]

                    # verifica quantidade de dados para saber se é possível rolar novamente
                    dados_suficientes = len(tubo_dados) < 3

                    if jogar and not dados_suficientes:
                        tubo_dados = self.gerar_tubo_embaralhado()

        # caso não haja vencedor por capturar 13 cérebros encontra o último sobrevivente
        if vencedor == '':
            for jogador in jogadores:
                if jogadores[jogador]['tiros'] < 3:
                    vencedor = jogador

        print(f"\n{vencedor} foi o zumbi vencedor desta partida!\n")

        if self.verifica_jogar_novamente():
            self.jogar()