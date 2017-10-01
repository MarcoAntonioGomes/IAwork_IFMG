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

    return (distX + distY)


def inTupla(tup, lista):
    for aux in lista:
        if(tup[0] == aux[0] and tup[1] == aux[1]):
            return True

def listaDirecao(fechada):
    direcao = list()
    print(fechada)
    for i in range (len(fechada)-1):

        if fechada[i][0] > fechada[i+1][0]:
            direcao.append("CIMA")
        if fechada[i][0] < fechada[i+1][0]:
            direcao.append("BAIXO")
        if fechada[i][1] > fechada[i+1][1]:
            direcao.append("ESQUERDA")
        if fechada[i][1] < fechada[i+1][1]:
            direcao.append("DIREITA")

    print(direcao)
    return direcao

def FindPath(start, finish, map):
    aberta = list()
    fechada = list()
    vizinho = list()
    star = list(start)
    star[4] = CalculateH(start, finish)
    star[5] = 0
    star2 = tuple(star)
    start = star2
    aberta.append(start)
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


                '''elif (atual[5] + map[vizinho[i][0]][vizinho[i][1]] <= vizLista[5]):
                    viz = list(vizinho[i])
                    print("ELIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIF")
                    viz[5] = atual[5] + map[vizinho[i][0]][vizinho[i][1]]
                    viz[4] = map[vizinho[i][0]][vizinho[i][1]] + CalculateH(vizinho, finish)
                    viz[2] = atual[0]
                    viz[3] = atual[1]
                    viz2 = tuple(viz)
                    vizinho[i] = viz2'''
