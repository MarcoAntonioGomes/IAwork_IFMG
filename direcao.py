from dbz import DragonballZ


def escolhedirecao(agente):
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

    # norte
    for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1]-i] == 1
            custo += 1
        elif mapa[agente_pos[0] - i][agente_pos[1]-i] == 2
            custo += 10
        else:
            custo += 35

    ranking.append((1, custo))
    # reseta custo
    custo = 0
    # nordeste
    for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1]-i] == 1
            custo += 1
        elif mapa[agente_pos[0]][agente_pos[1]-i] == 2
            custo += 10
        else:
            custo += 35
    for i in range(3):
        if mapa[agente_pos[0]+1][agente_pos[1]] == 1
            custo += 1
        elif mapa[agente_pos[0]+i][agente_pos[1]] == 2
            custo += 10
        else:
            custo += 35

    ranking.append((2, custo))
    # reseta custo
    custo = 0
    # leste
    for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1] + i] == 1
            custo += 1
        elif mapa[agente_pos[0]][agente_pos[1] + i] == 2
            custo += 10
        else:
            custo += 35

    ranking.append((3, custo))
    # reseta custo
    custo = 0
    # suldeste
        for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1] + i] == 1
            custo += 1
        elif mapa[agente_pos[0]][agente_pos[1] + i] == 2
            custo += 10
        else:
            custo += 35


    for i in range(3):
        if mapa[agente_pos[0] + i][agente_pos[1]] == 1
            custo += 1
        elif mapa[agente_pos[0] + i][agente_pos[1]] == 2
            custo += 10
        else:
            custo += 35



    ranking.append((4, custo))
    # reseta custo
    custo = 0
    # sul
    for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1] +i] == 1
            custo += 1
        elif mapa[agente_pos[0]][agente_pos[1] +i] == 2
            custo += 10
        else:
            custo += 35

    ranking.append((5, custo))
    # reseta custo
    custo = 0
    # suldoeste
    for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1] +i] == 1
            custo += 1
        elif mapa[agente_pos[0]][agente_pos[1] +i] == 2
            custo += 10
        else:
            custo += 35

    for i in range(3):
        if mapa[agente_pos[0]-i][agente_pos[1]] == 1
            custo += 1
        elif mapa[agente_pos[0]-i][agente_pos[1]] == 2
            custo += 10
        else:
            custo += 35

    ranking.append((6, custo))
    # reseta custo
    custo = 0
    # oeste
    for i in range(3):
        if mapa[agente_pos[0] - i][agente_pos[1]] == 1
            custo += 1
        elif mapa[agente_pos[0] - i][agente_pos[1]] == 2
            custo += 10
        else:
            custo += 35

    ranking.append((7, custo))
    # reseta custo
    custo = 0
    # noroeste
    for i in range(3):
        if mapa[agente_pos[0] - i][agente_pos[1]] == 1
            custo += 1
        elif mapa[agente_pos[0] - i][agente_pos[1]] == 2
            custo += 10
        else:
            custo += 35

    for i in range(3):
        if mapa[agente_pos[0]][agente_pos[1] - i] == 1
            custo += 1
        elif mapa[agente_pos[0]][agente_pos[1] - i] == 2
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
    elif ranking [0][0] == 2
        direcao = "nordeste"
    elif ranking [0][0] == 3
        direcao = "leste"
    elif ranking [0][0] == 4
        direcao = "suldeste"
    elif ranking [0][0] == 5
        direcao = "sul"
    elif ranking [0][0] == 6
        direcao = "suldoeste"
    elif ranking [0][0] == 7
        direcao = "oeste"
    elif ranking [0][0] == 8
        direcao = "nordeste"
    else:
        direcao = "erro"

    #retorna direcao escolhida
    return direcao


def anda(agente):

    #escolhe direcao
    direcao=escolhedirecao(agente)

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
        pos=agent_pos[0] + 3, agente_pos[1] + 3
    elif direcao == "suldoeste":
        pos=agente_pos[0] - 3, agente_pos[1] + 3
    else direcao == "erro":
        raise Exception("Erro ao passar a direcao com menor caminho")

    posfinal = pos

    return posfinal
