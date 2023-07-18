def consulta(contato):
    f = open('dados.txt', 'r') #primeiro parametro nome, segundo parametro modo (read)
    linhas = f.readlines()
    for linha in linhas:
        linha = linha.replace("\n","")
        nome, fone = linha.split(",")
        if contato == nome:
            print(nome, fone)
    f.close()

#consulta('Maria')


def insere(nome, fone):
    f = open('dados.txt', 'a') #parâmetro "a" permita apenas adicionar
    linha = nome+","+fone+"\n"
    f.writelines(linha)
    f.close()


#insere('Pedro', '3271-3000')


def delete(contato):
    f = open('dados.txt', 'r')
    linhas = f.readlines()
    linhas2 = []
    for linha in linhas:
        aux = linha
        linha = linha.replace("\n","")
        nome, fone = linha.split(",")
        if contato == nome:
            pass
        else:
            linhas2.append(aux)
    f.close()
    f = open('dados.txt', 'w') #permite escrever "w"
    f.writelines(linhas2)
    f.close()


def update(contato, fone2):
    f = open('dados.txt', 'r')
    linhas = f.readlines()
    linhas2 = []
    for linha in linhas:
        aux = linha
        linha = linha.replace("\n", "")
        nome, fone = linha.split(",")
        if contato == nome:
            linhas2.append(nome+','+fone2+'\n')
        else:
            linhas2.append(aux)
    f.close()
    f = open('dados.txt', 'w')  # permite escrever "w"
    f.writelines(linhas2)
    f.close()


#delete('Carlos')
update('Maria', "0000-0000")