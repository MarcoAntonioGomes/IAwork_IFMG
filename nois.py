from random import seed, random
"""
lista = (1, 2, 3, 4, 5, 6, 7, 8)


i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1
"""
"""
tamanho = 50
casa_kame = (int(random() * tamanho), int(random() * tamanho))

print(casa_kame)

casa_kame = casa_kame[0] + 3, casa_kame[1]

print(casa_kame)
"""


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
    inicio = CalculateH(start, finish)
    print(start)
    print(inicio)
    start = list(start)
    start.append(inicio)
    print(start)
    start = tuple(start)
    print(start)

    aberta.append(start)
    print(aberta)

    while(1):
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
                        break

        vizinho.append((atual[0], atual[1] - 1))
        vizinho.append((atual[0] - 1, atual[1]))
        vizinho.append((atual[0], atual[1] + 1))
        vizinho.append((atual[0] + 1, atual[1]))

        for i in range(4):
            if ((vizinho[i][0] >= 0 and vizinho[i][0] <= 6) and (vizinho[i][1] >= 0 and vizinho[i][1] <= 6) and not (vizinho[i] in fechada)):
                if(not vizinho[i] in aberta):
                    vizinho[i][2] = atual[0]
                    vizinho[i][3] = atual[1]

                    vizinho[i][4] = map[vizinho[i][0]][vizinho[i][1]] + CalculateH(vizinho, finish)
                    vizinho[i][5] = map[vizinho[i][0]][vizinho[i][1]] + atual[5]
                    aberta.append(vizinho[i])

                elif ((vizinho[i] in aberta) and (atual[5] + map[vizinho[i][0]][vizinho[i][1]] < vizinho[i][5])):
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
            Mat[i][j] = lista[x]
            x = x + 1

    a = (3, 3)
    b = (0, 6)

    FindPath(a, b, Mat)
