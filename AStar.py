
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
    print(start)

    while(True):
        print("Aberta=", aberta)
        aberta = sorted(aberta, key=lambda x: x[4])
        atual = aberta[0]
        print("Atual=", atual)
        del(aberta[0])
        fechada.append(atual)
        print("Aberta=", aberta)
        print("Fechada=", fechada)

        if((atual[0] == finish[0]) and (atual[1] == finish[1])):
            aux = atual
            print("Cheguei no destino...")
            while(aux[5] != 0):
                print("(", aux[0], ", ", aux[1], ", ", aux[5], ")\n")
                for aux2 in fechada:
                    if((aux[2] == aux2[0]) and (aux[3] == aux2[1])):
                        aux = aux2
                        break

        vizinho.append((atual[0], atual[1] - 1, 99, 99, 0, 0))
        vizinho.append((atual[0] - 1, atual[1], 99, 99, 0, 0))
        vizinho.append((atual[0], atual[1] + 1, 99, 99, 0, 0))
        vizinho.append((atual[0] + 1, atual[1], 99, 99, 0, 0))
        print("Vizinho=", vizinho)

        for i in range(4):
            print("Primeiro if=", vizinho[i][0] >= 0 and vizinho[i][0] <= 6, "2=", vizinho[i][1] >= 0 and vizinho[i][1] <= 6, "3=", not (vizinho[i] in fechada))
            if ((vizinho[i][0] >= 0 and vizinho[i][0] <= 6) and (vizinho[i][1] >= 0 and vizinho[i][1] <= 6) and not (vizinho[i] in fechada)):
                if(not vizinho[i] in aberta):
                    viz = list(vizinho[i])
                    print("Vizinho-", i, "=", viz)
                    viz[2] = atual[0]
                    viz[3] = atual[1]
                    viz[4] = map[viz[0]][viz[1]] + CalculateH(viz, finish)
                    viz[5] = map[viz[0]][viz[1]] + atual[5]
                    print("Vizinho-", i, "=", viz)

                    viz2 = tuple(viz)
                    vizinho[i] = viz2
                    print("Vizinho-", i, "=", vizinho[i])

                    aberta.append(vizinho[i])
                    print("Aberta=", aberta)

                elif ((vizinho[i] in aberta) and (atual[5] + map[vizinho[i][0]][vizinho[i][1]] < vizinho[i][5])):
                    print("Entrou no elif")
                    vizinho[i][5] = atual[5] + map[vizinho[i][0]][vizinho[i][1]]
                    vizinho[i][4] = map[vizinho[i][0]][vizinho[i][1]] + CalculateH(vizinho, finish)
                    vizinho[i][2] = atual[0]
                    vizinho[i][3] = atual[1]


if __name__ == "__main__":
    # matriz 7,7

    Mat = [None] * 7
    for i in range(7):
        Mat[i] = [None] * 7

    lista = list()

    # le o arquivo e pega o mapa
    for ln in open("MatrizTeste.txt"):
        ln = ln.split()
        lista.append(ln[0])

    # x é para percorrer a lista
    x = 0
    # preenche matriz com valores lista
    for i in range(7):
        for j in range(7):
            Mat[i][j] = int(lista[x])
            x = x + 1

    a = (3, 3, 3, 3, 0, 0)
    b = (0, 6, 0, 0, 0, 0)

    FindPath(a, b, Mat)
