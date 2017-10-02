buffer = ""

def converter(start, finish):
    print("Start=", start, "Finish=", finish)
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
    print("Start=", start, "Finish=", finish)
    finish = converter(start, finish)
    print("Finish=", finish)
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


def Direcao(radar):
    global buffer

    if(buffer == ""):
        if(radar["norte"] == 1):
            buffer = "norte"
        if(radar["nordeste"] == 1):
            buffer = "nordeste"
        if(radar["leste"] == 1):
            buffer = "leste"
        if(radar["suldeste"] == 1):
            buffer = "suldeste"
        if(radar["sul"] == 1):
            buffer = "sul"
        if(radar["suldoeste"] == 1):
            buffer = "suldoeste"
        if(radar["oeste"] == 1):
            buffer = "oeste"
        if(radar["noroeste"] == 1):
            buffer = "noroeste"

    if(buffer == "norte"):
        if(radar["norte"] == 1):
            buffer = "norte"
            return buffer

        if(radar["nordeste"] == 1):
            buffer = "nordeste"
            return buffer

        if(radar["noroeste"] == 1):
            buffer = "noroeste"
            return buffer

    if(buffer == "nordeste"):
        if(radar["nordeste"] == 1):
            buffer = "nordeste"
            return buffer

        if(radar["leste"] == 1):
            buffer = "leste"
            return buffer

        if(radar["norte"] == 1):
            buffer = "norte"
            return buffer

    if(buffer == "leste"):
        if(radar["leste"] == 1):
            buffer = "leste"
            return buffer

        if(radar["nordeste"] == 1):
            buffer = "nordeste"
            return buffer

        if(radar["suldeste"] == 1):
            buffer = "suldeste"
            return buffer

    if(buffer == "suldeste"):
        if(radar["suldeste"] == 1):
            buffer = "suldeste"
            return buffer

        if(radar["leste"] == 1):
            buffer = "leste"
            return buffer

        if(radar["sul"] == 1):
            buffer = "sul"
            return buffer

    if(buffer == "sul"):
        if(radar["sul"] == 1):
            buffer = "sul"
            return buffer

        if(radar["suldeste"] == 1):
            buffer = "suldeste"
            return buffer

        if(radar["suldoeste"] == 1):
            buffer = "suldoeste"
            return buffer

    if(buffer == "suldoeste"):
        if(radar["suldoeste"] == 1):
            buffer = "suldoeste"
            return buffer

        if(radar["sul"] == 1):
            buffer = "sul"
            return buffer

        if(radar["oeste"] == 1):
            buffer = "oeste"
            return buffer

    if(buffer == "oeste"):
        if(radar["oeste"] == 1):
            buffer = "oeste"
            return buffer

        if(radar["suldoeste"] == 1):
            buffer = "suldoeste"
            return buffer

        if(radar["noroeste"] == 1):
            buffer = "noroeste"
            return buffer

    if(buffer == "noroeste"):
        if(radar["noroeste"] == 1):
            buffer = "noroeste"
            return buffer

        if(radar["oeste"] == 1):
            buffer = "oeste"
            return buffer

        if(radar["norte"] == 1):
            buffer = "norte"
            return buffer

    if(radar["norte"] == 1):
        buffer = "norte"
        return buffer
    if(radar["nordeste"] == 1):
        buffer = "nordeste"
        return buffer
    if(radar["leste"] == 1):
        buffer = "leste"
        return buffer
    if(radar["suldeste"] == 1):
        buffer = "suldeste"
        return buffer
    if(radar["sul"] == 1):
        buffer = "sul"
        return buffer
    if(radar["suldoeste"] == 1):
        buffer = "suldoeste"
        return buffer
    if(radar["oeste"] == 1):
         buffer = "oeste"
         return buffer
    if(radar["noroeste"] == 1):
        buffer = "noroeste"
        return buffer

def Anda(radar, agentePos, mapa):
    dir = Direcao(radar)
    print("Entra na funcao=", agentePos)
    print("Dir=", dir)
    pos = list()
    pos.append(5)
    pos.append(5)
    i = 3

    if(dir == "norte"):
        while(True):
            pos[0] = agentePos[0]
            pos[1] = agentePos[1] - i
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "nordeste"):
        while(True):
            pos[0] = agentePos[0] + i
            pos[1] = agentePos[1] - i
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "leste"):
        while(True):
            pos[0] = agentePos[0] + i
            pos[1] = agentePos[1]
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "suldeste"):
        while(True):
            pos[0] = agentePos[0] + i
            pos[1] = agentePos[1] + i
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "sul"):
        while(True):
            pos[0] = agentePos[0]
            pos[1] = agentePos[1] + i
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "suldoeste"):
        while(True):
            pos[0] = agentePos[0] - i
            pos[1] = agentePos[1] + i
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "oeste"):
        while(True):
            pos[0] = agentePos[0] - i
            pos[1] = agentePos[1]
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break

    if(dir == "noroeste"):
        while(True):
            pos[0] = agentePos[0] - i
            pos[1] = agentePos[1] - i
            i = i - 1
            if(aceito([0,0], [len(mapa) - 1, len(mapa) - 1], agentePos)):
                break


    print("Sai da funcao=", agentePos)
    return tuple(pos)



