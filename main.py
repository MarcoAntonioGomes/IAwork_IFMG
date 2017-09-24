from dbz import *
from cosmetico import *


def dummy_agent(info):
    return DIREITA


if __name__ == "__main__":
    dbz = DragonBallZ(dummy_agent)
    executar_jogo(dbz)
