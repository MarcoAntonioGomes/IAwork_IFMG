# start é uma tupla do ponto inicial
# finish tupla do ponto destino
# map é o mapa do que Gohan consegue ver


def CalculateH(start, finish):
    distX = finish[0] - start[0]
    if(distX < 0):
        distX = distX * -1

    distY = finish[1] - start[1]
    if(distY < 0):
        distY = distY * -1

    return distX + distY


def FindPath(start, finish, map):
    aberta = list()
    fechada = list()
    vizinho = list()
    peso = list()
    aberta.append(start)
    peso.append(0)

    while(1):
        index = peso.index(min(peso))
        atual = aberta[index]
        del(aberta[index])
        fechada.append(atual)

        if(atual == finish):
            return

        vizinho.append((atual[0], atual[1] - 1))
        vizinho.append((atual[0] - 1, atual[1]))
        vizinho.append((atual[0], atual[1] + 1))
        vizinho.append((atual[0] + 1, atual[1]))

        for z in range(4):
            if (vizinho[z][0] < 0 & & vizinho[z][0] > 6):








           if(atual[1] > 0):
            # detro do limite
            esquerda = true
            # vizinho.append((atual[0] - 1, atual[1]))
        if(atual[1] < 6):
            # dentro do limite
            direita = true

            # vizinho.append((atual[0], atual[1] + 1))
        if(atual[])
