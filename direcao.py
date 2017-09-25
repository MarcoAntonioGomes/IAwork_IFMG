from dbz import DragonballZ


def escolhedirecao(agente):
    # joga a* em todos  os pontos onde
    # a flag da esfera for true
    # onde tiver o menor peso
    # joga para o anda

    return radar_direcao


def anda(agente):

    direcao = escolhedirecao(agente)
    if direcao == "norte":
        pos = agente_pos[0] - 3, agente_pos[1]
    elif direcao == "sul":
        pos = agente_pos[0] + 3, agente_pos[1]
    elif direcao == "leste":
        pos = agente_pos[0], agente_pos[1] + 3
    elif direcao == "oeste":
        pos = agente_pos[0], agente_pos[1] - 3
    elif direcao == "nordeste":
        pos = agente_pos[0] - 3, agente_pos[1] + 3
    elif direcao == "noroeste":
        pos = agente_pos[0] - 3, agente_pos[1] - 3
    elif direcao == "suldeste":
        pos = agent_pos[0] + 3, agente_pos[1] + 3
    elif direcao == "suldoeste":
        pos = agente_pos[0] + 3, agente_pos[1] - 3

    return pos
