from random import seed,random
tangentefixed = list()

def verificatangente(Listtangentefix,radar_direcao)
    if list

def vaientrar(Listtangentefix)
    if Listtangentefix != [] :
        return True
    else:
        return False


def prioridade(mapa,radar_direcao,agente_pos)


    tangente = list()

    """
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
    norte = 128
    nordeste = 123
    leste = 234
    suldeste = 345
    sul = 456
    suldeste = 567
    oeste = 678
    noroeste = 781
    """

    # norte
    if (radar_direcao["norte"]== 1):
        tangente.append(8,1,2)
    # nordeste
    if (radar_direcao["nordeste" ]== 1):
        tangente.append(1,2,3)
    # leste
    if (radar_direcao["leste" ]== 1):
        tangente.append(2,3,4)
    # suldeste
    if (radar_direcao["suldeste" ]== 1):
        tangente.append(3,4,5)
    # sul
    if (radar_direcao["sul" ]== 1):
        tangente.append(4,5,6)
    # suldoeste
    if (radar_direcao["suldoeste" ]== 1):
        tangente.append(5,6,7)
    # oeste
    if (radar_direcao["oeste" ]== 1):
        tangente.append(6,7,8)
     # noroeste
    if (radar_direcao["noroeste" ]== 1):
        tangente.append(7,8,1)

    quemvai = random.randint(0,len(tangente)-1)

    tangenteprioritaria = tangente[quemvai]
    global tangentefixed = tangenteprioritaria

    return tangenteprioritaria



def anda(mapa,radar_direcao,agente_pos)
    vaientrar(tangentefixed == False):
        prioridade(mapa,radar_direcao,agente_pos)




