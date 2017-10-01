
def converter(start, finish):
    fin = list(finish)
    fin[0] = finish[0] - start[0] + 3
    fin[1] = finish[1] - start[1] + 3
    fin2 = tuple(fin)

    return fin2

def CalculateH(start, finish):
    distX = finish[0] - start[0]
    if(distX < 0):
        distX = distX * -1

    distY = finish[1] - start[1]
    if(distY < 0):
        distY = distY * -1

    return (distX + distY)


def inTupla(tup, lista):
    for aux in lista:
        if(tup[0] == aux[0] and tup[1] == aux[1]):
            return True

def listaDirecao(fechada):
    direcao = list()
    print(fechada)
    for i in range (len(fechada)-1):

        #cima
        if fechada[i][0] > fechada[i+1][0]:
            direcao.append(3)
        #
        if fechada[i][0] < fechada[i+1][0]:
            direcao.append(4)
        #
        if fechada[i][1] > fechada[i+1][1]:
            direcao.append(1)
        #
        if fechada[i][1] < fechada[i+1][1]:
            direcao.append(2)

    print(direcao)
    return direcao

def FindPath(start, finish, map):
    finish = converter(start, finish)
    inn = (3,3,0,0,0,0)
    aberta = list()
    fechada = list()
    vizinho = list()
    star = list(inn)
    star[4] = CalculateH(inn, finish)
    star[5] = 0
    star2 = tuple(star)
    inn = star2
    aberta.append(inn)
    achou = False

    while(not achou):
        aberta = sorted(aberta, key=lambda x: x[4])
        atual = aberta[0]
        del(aberta[0])
        fechada.append(atual)

        if((atual[0] == finish[0]) and (atual[1] == finish[1])):
            aux = atual
            while(aux[5] != 0):
                print("(", aux[0], ", ", aux[1], ", ", aux[5], ")\n")
                for aux2 in fechada:
                    if((aux[2] == aux2[0]) and (aux[3] == aux2[1])):
                        aux = aux2
                        achou = True
                        break

        vizinho = list()
        vizinho.append((atual[0], atual[1] - 1, atual[0], atual[1], 0, 0))
        vizinho.append((atual[0] - 1, atual[1], atual[0], atual[1], 0, 0))
        vizinho.append((atual[0], atual[1] + 1, atual[0], atual[1], 0, 0))
        vizinho.append((atual[0] + 1, atual[1], atual[0], atual[1], 0, 0))


        for i in range(4):
            if ((vizinho[i][0] >= 0 and vizinho[i][0] <= 6) and (vizinho[i][1] >= 0 and vizinho[i][1] <= 6) and not inTupla(vizinho[i], fechada)):
                if(not inTupla(vizinho[i], aberta)):
                    viz = list(vizinho[i])
                    viz[2] = atual[0]
                    viz[3] = atual[1]
                    viz[4] = map[viz[0]][viz[1]] + CalculateH(viz, finish)
                    viz[5] = map[viz[0]][viz[1]] + atual[5]

                    viz2 = tuple(viz)
                    vizinho[i] = viz2

                    aberta.append(vizinho[i])



    return listaDirecao(fechada)


def aceito(limite_superior,limite_inferior,p):
    if(p[0]>=limite_superior[0] and p[1]>=limite_superior[1] and p[0] <= limite_inferior[0] and p[1]<= limite_inferior[1]):
        return True
    else:
        return False



def escolhedirecao(mapa,radar_direcao,agente_pos):
    """
    algoritmo passa a direção e o peso
    (dir,peso). Ex : [(1,10), (2,35)]
    uma lista ordena  pelo menor peso e vai passando
    ----------------------------------------
    1 = norte
    2 = nordeste
    3 = leste
    4 = suldeste
    5 = sul
    6 = suldoeste
    7 = oeste
    8 = noroeste

    -----------------------------------------
    norte pega as 3 casas a cima da pos atual
    nordeste pega em L ou seja 3 para a direita e 3 para cima 3 ou 3 para cima e 3 para o lado
    leste 3 para direita
    suldeste em L  3 para direita e 3 para baixo ou 3 p baixo 3 p direita
    sul 3 p baixo
    suldoeste 3 p esquerda 3 p baixo ou 3 p baixo e 3 p esquerda
    oeste 3 p esquerda
    noroeste 3 p esquerda e 3 p cima, ou 3 p cima e 3 p esquerda
    """
    # lista de tuplas
    ranking = list()
    custo = 0
    # norte
    if (radar_direcao["sul"]== 1):
        for i in range(3):
            if mapa[agente_pos[0]][agente_pos[1]-i] == 1 :
                custo += 1
            elif mapa[agente_pos[0] - i][agente_pos[1]-i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((1, custo))
        # reseta custo
        custo = 0
    # nordeste
    if (radar_direcao["nordeste" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0]+i][agente_pos[1]-i] == 1:
                custo += 1
            elif mapa[agente_pos[0]+i][agente_pos[1]-i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((2, custo))
        # reseta custo
        custo = 0
    # leste
    if (radar_direcao["leste" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0]][agente_pos[1] + i] == 1:
                custo += 1
            elif mapa[agente_pos[0]][agente_pos[1] + i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((3, custo))
        # reseta custo
        custo = 0
    # suldeste
    if (radar_direcao["suldeste" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0]+i][agente_pos[1] + i] == 1:
                custo += 1
            elif mapa[agente_pos[0]+i][agente_pos[1] + i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((4, custo))
        # reseta custo
        custo = 0
    # sul
    if (radar_direcao["norte" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0]][agente_pos[1] +i] == 1:
                custo += 1
            elif mapa[agente_pos[0]][agente_pos[1] +i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((5, custo))
        # reseta custo
        custo = 0
        # suldoeste
    if (radar_direcao["suldoeste" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0]-i][agente_pos[1] +i] == 1:
                custo += 1
            elif mapa[agente_pos[0]-i][agente_pos[1] +i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((6, custo))
        # reseta custo
        custo = 0
        # oeste
    if (radar_direcao["oeste" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0] - i][agente_pos[1]] == 1:
                custo += 1
            elif mapa[agente_pos[0] - i][agente_pos[1]] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((7, custo))
        # reseta custo
        custo = 0
    # noroeste
    if (radar_direcao["noroeste" ]== 1):
        for i in range(3):
            if mapa[agente_pos[0] - i][agente_pos[1] - i] == 1:
                custo += 1
            elif mapa[agente_pos[0] - i][agente_pos[1] - i] == 2:
                custo += 10
            else:
                custo += 35

        ranking.append((8, custo))
        # reseta custo
        custo = 0

    # ordena as direções pelo menor peso
    ranking.sort(key=lambda x: x[1])

    #escolhe direcao
    if ranking[0][0] == 1 :
        direcao = "norte"
    elif ranking [0][0] == 2:
        direcao = "nordeste"
    elif ranking [0][0] == 3:
        direcao = "leste"
    elif ranking [0][0] == 4:
        direcao = "suldeste"
    elif ranking [0][0] == 5:
        direcao = "sul"
    elif ranking [0][0] == 6:
        direcao = "suldoeste"
    elif ranking [0][0] == 7:
        direcao = "oeste"
    elif ranking [0][0] == 8:
        direcao = "nordeste"
    else:
        direcao = "erro"

    #retorna direcao escolhida
    return direcao


def anda(radar_direcao,mapa,agente_pos):

    while(True):
        #escolhe direcao
        direcao = escolhedirecao(mapa,radar_direcao,agente_pos)
        print("Direcao=", direcao)
        print("agente=", agente_pos)
        #anda a direcao
        if direcao == "norte":
            pos=agente_pos[0], agente_pos[1] - 3
        elif direcao == "sul":
            pos=agente_pos[0], agente_pos[1] + 3
        elif direcao == "leste":
            pos=agente_pos[0] + 3, agente_pos[1]
        elif direcao == "oeste":
            pos=agente_pos[0] - 3, agente_pos[1]
        elif direcao == "nordeste":
            pos=agente_pos[0] + 3, agente_pos[1] - 3
        elif direcao == "noroeste":
            pos=agente_pos[0] - 3, agente_pos[1] - 3
        elif direcao == "suldeste":
            pos=agente_pos[0] + 3, agente_pos[1] + 3
        elif direcao == "suldoeste":
            pos=agente_pos[0] - 3, agente_pos[1] + 3
        else:
            raise Exception("Erro ao passar a direcao com menor caminho")

        posfinal = pos
        print("posFinal=", posfinal)

        if(aceito([0,0],[len(mapa),len(mapa)],posfinal) == True):
            print("brecou")
            break

    return posfinal
